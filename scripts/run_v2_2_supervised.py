#!/usr/bin/env python3
"""One authorised, supervised Core pilot; no automatic retry or continuation.

Separate from the locked MCP draft. Native permissions are not full isolation.
Raw captures stay outside Git until the experimental orchestrator reviews them.
"""
import argparse
import json
from pathlib import Path
import tempfile
import time

import run_v2_2 as relay
from v2_2_transport import capture_process, local_cli

RUN_ID = "astra-medium-core-v2-2-supervised-001"
MANIFEST = relay.ROOT / "governance/v2-2-supervised.json"


def validate_manifest():
    manifest = json.loads(MANIFEST.read_text())
    if (manifest["run_id"] != RUN_ID or manifest["challenge"] != "calculator"
            or manifest["launch_authorized"] is not True
            or manifest["protocol_frozen"] is not True):
        raise PermissionError("This launcher authorises only the frozen Core pilot")
    for name, expected in manifest["inputs_sha256"].items():
        if relay.digest((relay.ROOT / name).read_bytes()) != expected:
            raise ValueError("Frozen input changed: " + name)
    return manifest


def prepare():
    manifest = validate_manifest()
    # A public reservation prevents this authorised identifier being relaunched.
    public = relay.ROOT / "runs" / RUN_ID
    public.mkdir()
    root = Path(tempfile.mkdtemp(prefix="agentbench-supervised-"))
    workspace = root / "workspace"
    (workspace / "solution").mkdir(parents=True)
    for relative in ("scripts/verify.py", "challenges/calculator/tests/test_acceptance.py"):
        destination = workspace / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes((relay.ROOT / relative).read_bytes())
    spec = (relay.ROOT / "challenges/calculator/SPEC.md").read_bytes()
    (workspace / "CHALLENGE.md").write_bytes(spec)
    (public / "CHALLENGE.md").write_bytes(spec)
    relay.save(public / "run.json", {"run_id": RUN_ID, "campaign": manifest["campaign"],
                                    "status": "prepared", "challenge": "calculator",
                                    "organisation": "V2.2-supervised", "exploratory": True})
    relay.save(root / "preparation.json", {"run_id": RUN_ID, "manifest_sha256": relay.digest(MANIFEST.read_bytes()),
                                          "baseline": relay.snapshot(workspace)})
    return root


def configuration(role):
    config = relay.config_for(role)
    config.update({"features.multi_agent": False, "features.apps": False,
                   "features.plugins": False, "features.hooks": False,
                   "features.code_mode_host": True,
                   "shell_environment_policy.inherit": "none",
                   "shell_environment_policy.set": {"PATH": "/usr/bin:/bin", "PYTHONDONTWRITEBYTECODE": "1"}})
    return config


def command(config, solution):
    # Build TOML scalars and inline tables separately; JSON objects aren't TOML.
    config = dict(config)
    environment = config.pop("shell_environment_policy.set")
    argv = relay.codex_command(config, solution)
    argv[0] = str(local_cli())
    table = "{" + ", ".join(f"{k}={json.dumps(v)}" for k, v in environment.items()) + "}"
    return ["/usr/bin/env", "-u", "OPENAI_API_KEY", "-u", "CODEX_API_KEY",
            "PYTHONDONTWRITEBYTECODE=1", *argv[:-1], "-c", "shell_environment_policy.set=" + table, "-"]


def run(root, transport=capture_process):
    validate_manifest()
    root = Path(root).resolve(strict=True)
    if root.is_relative_to(relay.ROOT) or relay.ROOT.is_relative_to(root):
        raise ValueError("Candidate workspace must be outside the repository")
    preparation = json.loads((root / "preparation.json").read_text())
    if preparation["run_id"] != RUN_ID or preparation["manifest_sha256"] != relay.digest(MANIFEST.read_bytes()):
        raise ValueError("Wrong preparation/manifest")
    workspace, capture = root / "workspace", root / "capture"
    if relay.snapshot(workspace) != preparation["baseline"]:
        raise ValueError("Prepared workspace changed before launch")
    capture.mkdir(mode=0o700)  # Exclusive: never resume or retry this attempt.
    solution = workspace / "solution"
    report = {"run_id": RUN_ID, "status": "running", "sessions": [], "attempts": [],
              "requested_model": "gpt-6-astra", "requested_effort": "medium",
              "exploratory": True, "full_isolation_claimed": False, "deviations": []}
    started, first = time.monotonic(), None
    try:
        for phase, role, mandate_name, limit in relay.PHASES:
            config = configuration(role)
            mandate = (relay.ROOT / "prompts" / mandate_name).read_text()
            # Canonical challenge bytes unchanged; only adapt its example path.
            mandate += ("\nPilote supervisé : le dossier courant est solution/. Ne crée aucun cache. "
                        "Le contrat est ../CHALLENGE.md. Pour P3 seulement, la commande officielle locale est "
                        "`python3 -B ../scripts/verify.py --solution .`\n"
                        "N'accède pas au dépôt original.\n")
            prompt = relay.make_prompt(mandate, (workspace / "CHALLENGE.md").read_text(), first, report["sessions"])
            argv = command(config, solution)
            before = relay.snapshot(workspace)
            attempt = {"phase": phase, "role": role, "status": "running", "config": config,
                       "prompt_sha256": relay.digest(prompt.encode())}
            report["attempts"].append(attempt)
            relay.save(capture / "state.json", report)
            print("Starting " + phase, flush=True)
            state = transport(argv, prompt, capture / phase, cwd=solution)
            attempt.update(status="captured", process=state)
            relay.save(capture / "state.json", report)
            raw = (capture / phase / "stdout.jsonl").read_text()
            # Preserve available counters even when strict parsing stops the run.
            events = [json.loads(line) for line in raw.splitlines() if line.strip()]
            attempt["observed_usage"] = [e.get("usage") for e in events if e.get("type") == "turn.completed"]
            if state["exit_code"] != 0:
                raise RuntimeError("Candidate process failed; inspect private capture")
            parsed = relay.parse_events(raw)
            if parsed["thread_id"] in {r["thread_id"] for r in report["sessions"]}:
                raise ValueError("Reused candidate thread")
            after = relay.snapshot(workspace)
            protected = lambda snap: {p: v for p, v in snap.items() if not p.startswith("solution/")}
            if protected(before) != protected(after) or (role == "REV-01" and before != after):
                raise PermissionError("Observed write outside role boundary")
            files = relay.snapshot(solution)
            if set(files) != relay.DELIVERABLES["calculator"]:
                raise ValueError("Missing or extra deliverable")
            record = {**parsed, "phase": phase, "role": role, "duration_seconds": state["duration_seconds"]}
            report["sessions"].append(record)
            attempt["status"] = "completed"
            if parsed["final_words"] > limit:
                report["deviations"].append({"phase": phase, "kind": "word_limit", "limit": limit, "observed": parsed["final_words"]})
            if first is None:
                first = files
                relay.save(capture / "snapshot-initial.json", first)
            relay.save(capture / "state.json", report)
        relay.save(capture / "snapshot-final.json", relay.snapshot(solution))
        report["status"] = "candidate_sessions_completed_pending_independent_verification"
    except BaseException as error:
        report.update(status="interrupted", failure={"type": type(error).__name__, "message": str(error)})
        raise
    finally:
        report["wall_duration_seconds"] = time.monotonic() - started
        relay.save(capture / "state.json", report)
    return report


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--prepare", action="store_true")
    mode.add_argument("--run", type=Path)
    args = parser.parse_args()
    print(prepare() if args.prepare else json.dumps(run(args.run), ensure_ascii=False))
