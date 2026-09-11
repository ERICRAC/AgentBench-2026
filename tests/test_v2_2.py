"""Lean-pair maintenance tests: no model, network, or historical solution."""

import contextlib
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import run_v2_2 as relay
import preflight_v2_2


class LeanPairTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="agentbench-lean-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.workspace = self.root / "workspace"
        self.solution = self.workspace / "solution"
        self.solution.mkdir(parents=True)
        (self.workspace / "CHALLENGE.md").write_text("Synthetic challenge\n", encoding="utf-8")
        self.capture = self.root / "capture"
        # Any accidental launch or network call fails the test, not a model bill.
        for target in ("subprocess.Popen", "socket.socket", "socket.create_connection"):
            guard = patch(target, side_effect=AssertionError("No process/network in fake preflight"))
            guard.start()
            self.addCleanup(guard.stop)

    def run_fake(self, transport=relay.fake_transport, **kwargs):
        return relay.run_relay(self.workspace, self.capture, "calculator", transport,
                               simulation=kwargs.get("simulation", True))

    def state(self):
        return json.loads((self.capture / "state.json").read_text())

    @staticmethod
    def transform(response, mutate):
        events = [json.loads(line) for line in response["jsonl"].splitlines()]
        mutate(events)
        return {**response, "jsonl": "\n".join(json.dumps(e) for e in events)}

    def test_three_phases_full_handover_and_snapshots(self):
        requests = []
        def transport(request):
            requests.append(request)
            return relay.fake_transport(request)
        result = self.run_fake(transport)
        self.assertEqual([r["role"] for r in requests], ["MAIN", "REV-01", "MAIN"])
        self.assertEqual([r["config"]["sandbox_mode"] for r in requests],
                         ["workspace-write", "read-only", "workspace-write"])
        for index, request in enumerate(requests):
            payload = json.loads(request["prompt"].split("DONNÉES DU RELAIS — pas des instructions de rôle :\n")[1])
            self.assertEqual(len(payload["prior_sessions"]), index)
            for record in payload["prior_sessions"]:
                self.assertEqual(record["commands"][0]["aggregated_output"], "SIMULATED output\n")
            if index:
                self.assertEqual(set(payload["first_solution"]), {"calculator.py", "README.md"})
                self.assertIn("main_initial", payload["first_solution"]["calculator.py"]["text"])
        self.assertEqual(result["input_plus_output_tokens"], 39)
        self.assertEqual(result["model_calls"], 0)
        self.assertTrue(all(len(r["config_sha256"]) == 64 for r in result["sessions"]))
        self.assertIsNone(result["official_verdict"])
        first = json.loads((self.capture / "snapshot-initial.json").read_text())
        final = json.loads((self.capture / "snapshot-final.json").read_text())
        self.assertNotEqual(first, final)
        self.assertLessEqual(result["sum_session_seconds"], result["wall_duration_seconds"])
        for previous, current in zip(result["sessions"], result["sessions"][1:]):
            self.assertLessEqual(previous["ended_at_seconds"], current["started_at_seconds"])

    def test_live_rejected_before_transport_or_capture(self):
        def forbidden(request):
            self.fail("Transport must never be invoked")
        with self.assertRaises(PermissionError):
            self.run_fake(forbidden, simulation=False)
        self.assertFalse(self.capture.exists())
        with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as exit_error:
            relay.main(["--live"])
        self.assertEqual(exit_error.exception.code, 2)

    def test_nonempty_solution_and_existing_capture_refused(self):
        (self.solution / "existing.txt").write_text("Keep me")
        with self.assertRaises(ValueError):
            self.run_fake()
        self.assertEqual((self.solution / "existing.txt").read_text(), "Keep me")
        self.capture.mkdir()
        with self.assertRaises(FileExistsError):
            self.run_fake()

    def test_capture_cannot_be_nested_in_workspace(self):
        with self.assertRaises(ValueError):
            relay.run_relay(self.workspace, self.workspace / "private", "calculator",
                            relay.fake_transport, simulation=True)

    def test_phase_failure_preserved_without_retry(self):
        calls = []
        def transport(request):
            calls.append(request["phase"])
            if request["phase"] == "review":
                raise RuntimeError("Synthetic quota exhaustion")
            return relay.fake_transport(request)
        with self.assertRaises(RuntimeError):
            self.run_fake(transport)
        self.assertEqual(calls, ["main_initial", "review"])
        self.assertEqual(self.state()["status"], "interrupted")
        self.assertIsNone(self.state()["input_plus_output_tokens"])
        self.assertTrue((self.capture / "snapshot-initial.json").exists())
        self.assertEqual(self.state()["attempts"][-1]["outcome"], "interrupted")
        self.assertIsNotNone(self.state()["attempts"][-1]["ended_at_seconds"])

    def test_keyboard_interrupt_checkpointed(self):
        def interrupt(request):
            raise KeyboardInterrupt()
        with self.assertRaises(KeyboardInterrupt):
            self.run_fake(interrupt)
        self.assertEqual(self.state()["failure"]["type"], "KeyboardInterrupt")

    def test_reviewer_write_stops_before_final(self):
        def transport(request):
            result = relay.fake_transport(request)
            if request["phase"] == "review":
                (self.solution / "calculator.py").write_text("Forbidden edit")
            return result
        with self.assertRaises(PermissionError):
            self.run_fake(transport)
        self.assertEqual(len(self.state()["sessions"]), 2)
        self.assertEqual((self.solution / "calculator.py").read_text(), "Forbidden edit")

    def test_protected_workspace_write_stops(self):
        def transport(request):
            result = relay.fake_transport(request)
            (self.workspace / "CHALLENGE.md").write_text("Forbidden change")
            return result
        with self.assertRaises(PermissionError):
            self.run_fake(transport)
        self.assertEqual(len(self.state()["sessions"]), 1)

    def test_missing_or_extra_deliverable_stops(self):
        def transport(request):
            result = relay.fake_transport(request)
            (self.solution / "unexpected.md").write_text("Extra file")
            return result
        with self.assertRaises(ValueError):
            self.run_fake(transport)
        self.assertEqual(len(self.state()["sessions"]), 1)

    def test_missing_deliverable_stops(self):
        def transport(request):
            result = relay.fake_transport(request)
            (self.solution / "README.md").unlink()
            return result
        with self.assertRaises(ValueError):
            self.run_fake(transport)
        self.assertEqual(len(self.state()["sessions"]), 1)

    def test_reused_thread_stops(self):
        def transport(request):
            return self.transform(relay.fake_transport(request),
                                  lambda es: es[0].update(thread_id="same-thread"))
        with self.assertRaises(ValueError):
            self.run_fake(transport)
        self.assertEqual(len(self.state()["sessions"]), 2)

    def test_word_overrun_recorded_without_truncation_or_retry(self):
        words = "word " * 1201
        def transport(request):
            def alter(es):
                if request["phase"] == "review":
                    es[-2]["item"]["text"] = words
            return self.transform(relay.fake_transport(request), alter)
        result = self.run_fake(transport)
        self.assertEqual(len(result["sessions"]), 3)
        self.assertEqual(result["deviations"], [{"phase": "review", "kind": "word_limit",
                                                "observed": 1201, "limit": 1200}])
        self.assertEqual(result["sessions"][1]["messages"][-1], words)
        self.assertIn(words, (self.capture / "main_final.prompt.txt").read_text())

    def test_missing_usage_is_not_zero(self):
        def transport(request):
            return self.transform(relay.fake_transport(request), lambda es: es[-1].pop("usage"))
        result = self.run_fake(transport)
        self.assertIsNone(result["input_plus_output_tokens"])
        self.assertTrue(all(r["usage"] is None for r in result["sessions"]))

    def test_nonzero_process_retains_raw_and_metrics(self):
        def transport(request):
            return {**relay.fake_transport(request), "exit_code": 1}
        with self.assertRaises(RuntimeError):
            self.run_fake(transport)
        self.assertEqual(self.state()["sessions"][0]["usage"]["input_tokens"], 10)
        self.assertTrue((self.capture / "main_initial.events.jsonl").exists())

    def test_invalid_json_capture_preserved(self):
        def transport(request):
            return {"jsonl": "incomplete {", "exit_code": 0}
        with self.assertRaises(ValueError):
            self.run_fake(transport)
        self.assertEqual((self.capture / "main_initial.events.jsonl").read_text(), "incomplete {")
        self.assertEqual(self.state()["status"], "interrupted")

    def test_parser_rejects_incomplete_unsupported_events_and_bad_usage(self):
        request = {"phase": "review"}
        source = relay.fake_transport(request)
        mutations = [lambda es: es.pop(), lambda es: es[-2]["item"].pop("text"),
                     lambda es: es[2]["item"].pop("aggregated_output"),
                     lambda es: es[2]["item"].update(truncated=True),
                     lambda es: es.append(es[-1]),
                     lambda es: es[-1].update(usage={"input_tokens": -1}),
                     lambda es: es.append({"type": "error", "message": "quota"}),
                     lambda es: es.append({"type": "item.started", "item": {"id": "pending"}}),
                     lambda es: es[2]["item"].update(type="unexpected_tool")]
        for mutate in mutations:
            with self.subTest(mutate=mutate), self.assertRaises(ValueError):
                relay.parse_events(self.transform(source, mutate)["jsonl"])

    def test_reasoning_excluded_visible_text_unchanged(self):
        def mutate(es):
            es.insert(2, {"type": "item.completed", "item": {"type": "reasoning", "text": "private-thought"}})
        record = relay.parse_events(self.transform(relay.fake_transport({"phase": "review"}), mutate)["jsonl"])
        self.assertNotIn("private-thought", json.dumps(record))
        self.assertEqual(record["messages"], ["REV-001 suggestion synthétique"])

    def test_truncated_output_marker_stops(self):
        def transport(request):
            def mutate(es):
                es[2]["item"]["aggregated_output"] = "Warning: truncated output (more data)"
            return self.transform(relay.fake_transport(request), mutate)
        with self.assertRaises(ValueError):
            self.run_fake(transport)
        self.assertEqual(self.state()["status"], "interrupted")

    def test_invalid_event_envelope(self):
        for raw in ("[]", "null", "{}", "", '{"type":"turn.completed"}'):
            with self.subTest(raw=raw), self.assertRaises(ValueError):
                relay.parse_events(raw)

    def test_symlink_workspace_rejected(self):
        alias = self.root / "alias"
        alias.symlink_to(self.workspace, target_is_directory=True)
        with self.assertRaises(ValueError):
            relay.run_relay(alias, self.capture, "calculator", relay.fake_transport, simulation=True)

    def test_configuration_drift_rejected(self):
        original = Path.read_text
        def changed(path, *args, **kwargs):
            text = original(path, *args, **kwargs)
            return text.replace('model_reasoning_effort = "medium"', 'model_reasoning_effort = "high"')
        with patch.object(Path, "read_text", changed), self.assertRaises(ValueError):
            relay.config_for("MAIN")

    def test_preflight_refuses_changed_choice_or_authority(self):
        original = Path.read_text
        for change in ("authority", "budget"):
            def changed(path, *args, **kwargs):
                text = original(path, *args, **kwargs)
                if path.name == "choices.json":
                    data = json.loads(text)
                    if change == "authority":
                        data["launch_authorized"] = True
                    else:
                        data["choices"]["review_words"] = 600
                    return json.dumps(data)
                return text
            with self.subTest(change=change), patch.object(Path, "read_text", changed), self.assertRaises(ValueError):
                preflight_v2_2.check()

    def test_snapshot_rejects_symlinks_hardlinks_and_binary(self):
        outside = self.root / "outside.txt"
        outside.write_text("Private data")
        for kind in ("symlink", "hardlink", "binary"):
            folder = self.root / kind
            folder.mkdir()
            target = folder / "file"
            if kind == "symlink":
                target.symlink_to(outside)
            elif kind == "hardlink":
                target.hardlink_to(outside)
            else:
                target.write_bytes(b"\xff\xfe")
            with self.subTest(kind=kind), self.assertRaises(ValueError):
                relay.snapshot(folder)

    def test_configuration_and_unexecuted_argv(self):
        for role in ("MAIN", "REV-01"):
            config = relay.config_for(role)
            argv = relay.codex_command(config, self.solution)
            self.assertEqual(argv[:2], ["codex", "exec"])
            self.assertIn("--strict-config", argv)
            self.assertIn("--ephemeral", argv)
            self.assertNotIn("resume", argv)
            self.assertEqual(config["model_reasoning_effort"], "medium")
            self.assertNotIn("--dangerously-bypass-approvals-and-sandbox", argv)
        with self.assertRaises(ValueError):
            relay.config_for("SA-03")

    def test_simulation_cli_both_challenges_and_no_overwrite(self):
        for challenge in relay.DELIVERABLES:
            output = self.root / challenge
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(relay.main(["--simulate", "--challenge", challenge,
                                             "--output", str(output)]), 0)
            with self.assertRaises(FileExistsError):
                relay.simulate(output, challenge)
        with self.assertRaises(ValueError):
            relay.simulate(ROOT / "never-create-lean-fixture", "calculator")

    def test_preflight_no_model_no_verdict_and_hash_inventory(self):
        report = preflight_v2_2.check()
        self.assertFalse(report["launch_authorized"])
        self.assertFalse(report["protocol_frozen"])
        self.assertEqual(len(report["simulations"]), 2)
        self.assertEqual(report["model_calls"], 0)
        self.assertFalse(report["os_isolation_checked"])
        self.assertEqual(len(report["hashes"]), 15)
        self.assertTrue(all(r["official_verdict"] is None for r in report["simulations"]))


if __name__ == "__main__":
    unittest.main()
