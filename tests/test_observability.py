"""Maintenance-only tests. No model calls, no candidate solutions modified."""

import contextlib
import hashlib
import io
import json
from pathlib import Path
import sys
import tempfile
import threading
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import attach_observations
import observe_sessions
import run_v2
import run_v2_observed
import summarize_runs


class ObservationTests(unittest.TestCase):
    def test_success_passes_arguments_and_return_unchanged(self):
        clock = iter([10.0, 10.25, 12.5])
        observer = observe_sessions.SessionObserver(lambda: next(clock))
        with tempfile.TemporaryDirectory() as directory:
            arguments = {"private_root": Path(directory), "prompt": "private text"}
            sentinel = object()
            def session(**kwargs):
                self.assertEqual(kwargs, arguments)
                return sentinel
            self.assertIs(observer.invoke(session, {"session_id": "any-agent"}, **arguments), sentinel)
            payload = json.loads((Path(directory) / "observations.json").read_text())
            event = payload["sessions"][0]
            self.assertEqual(event["started_at_seconds"], .25)
            self.assertEqual(event["ended_at_seconds"], 2.5)
            self.assertEqual(event["duration_seconds"], 2.25)
            self.assertNotIn("private text", json.dumps(payload))
            self.assertNotIn(directory, json.dumps(payload))

    def test_failure_is_persisted_and_propagated(self):
        observer = observe_sessions.SessionObserver()
        error = RuntimeError("private error text")
        with tempfile.TemporaryDirectory() as directory:
            def fail(**kwargs):
                raise error
            with self.assertRaises(RuntimeError) as raised:
                observer.invoke(fail, {"session_id": "failed"}, private_root=Path(directory))
            self.assertIs(raised.exception, error)
            text = (Path(directory) / "observations.json").read_text()
            self.assertEqual(json.loads(text)["sessions"][0]["outcome"], "failed")
            self.assertNotIn(str(error), text)

    def test_arbitrary_parallel_agents_are_not_serialised(self):
        observer = observe_sessions.SessionObserver()
        barrier = threading.Barrier(5)
        with tempfile.TemporaryDirectory() as directory:
            def session(**kwargs):
                barrier.wait(timeout=5)
            with run_v2.ThreadPoolExecutor(max_workers=5) as pool:
                futures = [pool.submit(observer.invoke, session, {"session_id": f"local-{i}"},
                                       private_root=Path(directory)) for i in range(5)]
                for future in futures:
                    future.result()
            events = json.loads((Path(directory) / "observations.json").read_text())["sessions"]
            self.assertEqual(len(events), 5)
            self.assertLess(max(e["started_at_seconds"] for e in events),
                            min(e["ended_at_seconds"] for e in events))

    def test_original_frozen_runner_and_publisher_hashes(self):
        for name, expected in {
            "run_v2.py": "3cb0f940ebc8fe0c422b948c35de4b00273815d3dc4cb91f04b53e62814f19c4",
            "publish_v2.py": "9c54d54bc726e9b8a4d5cfbd706b31d2f564e9c2c824b60c0d85de79bf34cb3b",
        }.items():
            self.assertEqual(hashlib.sha256((ROOT / "scripts" / name).read_bytes()).hexdigest(), expected)

    def test_full_sequence_prompts_arguments_and_barriers_unchanged(self):
        """Execute both real orchestration paths with the same fake candidates."""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            run = root / "runs" / "fixture"
            solution = run / "solution"
            solution.mkdir(parents=True)
            (run / "CHALLENGE.md").write_text("fixture challenge")
            (root / "prompts").mkdir()
            (root / "prompts/codex-multi.md").write_text("fixture mandate")
            for role in run_v2.ROLES:
                (run / f"config-{role.lower()}.toml").write_text('model = "fixture"\n')
            outputs = []
            for index, entry in enumerate((run_v2.main, run_v2_observed.main)):
                capture = root / f"private-{index}"
                capture.mkdir()
                calls, finished = {}, set()
                lock = threading.Lock()
                barriers = {"P1": threading.Barrier(2), "P2": threading.Barrier(2)}
                topology = observe_sessions.v2_topology()
                def fake(**kwargs):
                    spec = topology[kwargs["label"]]
                    with lock:
                        self.assertTrue(set(spec["depends_on"]).issubset(finished))
                        calls[kwargs["label"]] = {key: str(value) for key, value in kwargs.items()
                                                   if key != "private_root"}
                    if spec["parallel_group"]:
                        barriers[spec["parallel_group"]].wait(timeout=5)
                    with lock:
                        finished.add(spec["session_id"])
                    return {"thread_id": spec["session_id"], "duration_seconds": 1,
                            "usage": {"input_tokens": 2, "output_tokens": 3},
                            "visible_messages": ["reply " + kwargs["label"]]}
                with patch.object(run_v2, "ROOT", root), patch.object(run_v2, "run_session", fake), \
                     patch.object(run_v2.tempfile, "mkdtemp", return_value=str(capture)), \
                     patch.object(run_v2.subprocess, "check_output", return_value="fake-cli"), \
                     patch.object(sys, "argv", ["runner", "--run", str(run)]), \
                     contextlib.redirect_stdout(io.StringIO()):
                    self.assertEqual(entry(), 0)
                    self.assertIs(run_v2.run_session, fake)
                outputs.append(calls)
                self.assertEqual(len(calls), 7)
                self.assertFalse(any(solution.iterdir()))
                if index:
                    events = json.loads((capture / "observations.json").read_text())
                    trace = {"sessions": [{"phase": e["session_id"], "role": e["role"],
                                           "duration_seconds": 1} for e in events["sessions"]]}
                    merged = attach_observations.merge(trace, events)
                    self.assertEqual(len(merged["sessions"]), 7)
                    self.assertTrue(all(s["duration_seconds"] == 1 for s in merged["sessions"]))
            self.assertEqual(outputs[0], outputs[1])


class PublicationTests(unittest.TestCase):
    def fixture(self):
        trace = {"sessions": [{"phase": "local", "role": "OLLAMA", "duration_seconds": 1}]}
        observation = {"sessions": [{"session_id": "local", "role": "OLLAMA",
            "started_at_seconds": .5, "ended_at_seconds": 2, "duration_seconds": 1.5,
            "parallel_group": None, "depends_on": [], "receives_from": [],
            "writes_solution": False, "outcome": "returned", "private_prompt": "excluded"}]}
        return trace, observation

    def test_allowlist_and_original_duration_preserved(self):
        trace, observation = self.fixture()
        result = attach_observations.merge(trace, observation)
        self.assertNotIn("observation", trace["sessions"][0])
        self.assertNotIn("private_prompt", result["sessions"][0]["observation"])
        self.assertEqual(result["sessions"][0]["duration_seconds"], 1)
        self.assertEqual(result["sessions"][0]["observation"]["duration_seconds"], 1.5)

    def test_rejects_missing_duplicate_or_mismatched_sessions(self):
        for variation in ("missing", "duplicate", "role"):
            with self.subTest(variation=variation):
                trace, observation = self.fixture()
                if variation == "missing":
                    observation["sessions"] = []
                elif variation == "duplicate":
                    observation["sessions"] *= 2
                else:
                    observation["sessions"][0]["role"] = "WRONG"
                with self.assertRaises(ValueError):
                    attach_observations.merge(trace, observation)

    def test_rejects_invalid_times_and_dependencies(self):
        for change in ({"started_at_seconds": -1}, {"ended_at_seconds": float("nan")},
                       {"duration_seconds": 500}, {"depends_on": ["missing"]},
                       {"depends_on": ["local"]}, {"receives_from": ["missing"]}):
            with self.subTest(change=change):
                trace, observation = self.fixture()
                observation["sessions"][0].update(change)
                with self.assertRaises(ValueError):
                    attach_observations.merge(trace, observation)

    def test_merge_cli_does_not_overwrite(self):
        trace, observation = self.fixture()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "trace.json").write_text(json.dumps(trace))
            (root / "observation.json").write_text(json.dumps(observation))
            destination = root / "output.json"
            destination.write_text("do not change")
            with patch.object(sys, "argv", ["merge", "--trace", str(root / "trace.json"),
                        "--observations", str(root / "observation.json"), "--output", str(destination)]):
                with self.assertRaises(FileExistsError):
                    attach_observations.main()
            self.assertEqual(destination.read_text(), "do not change")

    def test_missing_metrics_are_not_zero_and_no_fake_timing(self):
        data = {"run_id": "fixture", "mode": "future", "usage": {"input_tokens": 5}}
        trace = {"roles": {"LOCAL-9": "Local reviewer"},
                 "sessions": [{"phase": "local-phase", "role": "LOCAL-9", "duration_seconds": 9}]}
        result = summarize_runs.render(data, trace, "Unassessed", "en")
        self.assertIn("LOCAL-9", result)
        self.assertIn("| Input + output tokens | Not recorded |", result)
        self.assertNotIn("SA-01", result)
        self.assertNotIn("0.000 / 9.000", result)

    def test_measured_timing_generic_role_and_no_counter_double_count(self):
        trace, observation = self.fixture()
        result = summarize_runs.render(
            {"run_id": "future", "usage": {"input_tokens": 10, "output_tokens": 5,
             "cached_input_tokens": 8, "reasoning_output_tokens": 3}},
            attach_observations.merge(trace, observation), "Unassessed", "en")
        self.assertIn("0.500 / 2.000", result)
        self.assertIn("| Input + output tokens | 15 |", result)
        self.assertIn("OLLAMA", result)

    def test_generated_pages_are_current(self):
        summarize_runs.generate(check=True)


if __name__ == "__main__":
    unittest.main()
