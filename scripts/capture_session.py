#!/usr/bin/env python3
"""Capture a fresh Codex session; keep raw events outside the public repository.

Use only as the experimental orchestrator. This is not a candidate tool.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import tempfile
import time
import tomllib

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--cwd", required=True, type=Path)
    parser.add_argument("--prompt", required=True, type=Path)
    parser.add_argument("--config", required=True, type=Path)
    args = parser.parse_args()
    config_bytes = args.config.read_bytes()
    config = tomllib.loads(config_bytes.decode())
    command = ["codex", "exec", "--strict-config", "--ignore-user-config",
               "--ignore-rules", "--ephemeral", "--json", "--skip-git-repo-check",
               "-C", str(args.cwd.resolve())]
    for key, value in config.items():
        if not isinstance(value, (str, int, bool)):
            parser.error("Only scalar configuration entries are supported")
        command.extend(["-c", f"{key}={json.dumps(value)}"])
    command.append("-")
    private = Path(tempfile.mkdtemp(prefix="agentbench-session-"))
    print(f"Private capture: {private}", flush=True)
    started = time.monotonic()
    env = os.environ.copy()
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    with (private / "events.jsonl").open("w") as out, (private / "stderr.txt").open("w") as err:
        completed = subprocess.run(command, input=args.prompt.read_text(), text=True,
                                   stdout=out, stderr=err, env=env, check=False)
    record = {"command": command, "config": config,
              "config_sha256": hashlib.sha256(config_bytes).hexdigest(),
              "prompt_sha256": hashlib.sha256(args.prompt.read_bytes()).hexdigest(),
              "duration_seconds": round(time.monotonic() - started, 3),
              "exit_code": completed.returncode,
              "cli_version": subprocess.check_output(["codex", "--version"], text=True).strip(),
              "thread_id": None, "usage": None, "visible_messages": [], "commands": []}
    for line in (private / "events.jsonl").read_text().splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        if event.get("type") == "thread.started":
            record["thread_id"] = event.get("thread_id")
        if event.get("type") == "turn.completed":
            record["usage"] = event.get("usage")
        if event.get("type") == "item.completed":
            item = event.get("item", {})
            if item.get("type") == "agent_message":
                record["visible_messages"].append(item.get("text", ""))
            if item.get("type") == "command_execution":
                record["commands"].append({key: item.get(key) for key in
                                           ("command", "aggregated_output", "exit_code")})
    (private / "record.json").write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({key: record[key] for key in
                      ("exit_code", "thread_id", "duration_seconds", "usage")}), flush=True)
    raise SystemExit(completed.returncode)


if __name__ == "__main__":
    main()
