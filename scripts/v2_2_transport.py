#!/usr/bin/env python3
"""Private subprocess capture and least-privilege Codex command profiles.

This is transport infrastructure, not launch authority. No model is called by
this module or its preflight. The draft relay's live lock remains in force.
"""

from __future__ import annotations

import json
import os
from pathlib import Path
import shutil
import signal
import subprocess
import time

import run_v2_2 as relay


def permissions(role: str, workspace: Path, cli: Path) -> list[str]:
    """Same explicit profile for local OS probes and prepared model commands.

    No root/home/tmp wildcard access. Runtime paths come from Codex :minimal;
    the standalone CLI must itself be readable to enter its Linux sandbox.
    Profiles must NOT be combined with the legacy sandbox_mode setting.
    """
    if role not in {"MAIN", "REV-01"}:
        raise ValueError("Unknown role")
    workspace = Path(workspace)
    cli = Path(cli)
    if workspace.is_symlink() or (workspace / "solution").is_symlink():
        raise ValueError("Linked workspace or solution")
    workspace, cli = workspace.resolve(strict=True), cli.resolve(strict=True)
    if not workspace.is_dir() or not (workspace / "solution").is_dir() or not cli.is_file():
        raise ValueError("Missing workspace, solution or CLI")
    paths = {":minimal": "read", ":slash_tmp": "deny", ":tmpdir": "deny",
             str(cli): "read", str(workspace): "read",
             str(workspace / "solution"): "write" if role == "MAIN" else "read"}
    table = "{" + ", ".join(f"{json.dumps(k)}={json.dumps(v)}" for k, v in paths.items()) + "}"
    return ["-P", "agentbench-v2-2", "-c",
            f"permissions.agentbench-v2-2.filesystem={table}", "-c",
            "permissions.agentbench-v2-2.network.enabled=false"]


def prepared_command(role: str, workspace: Path, cli: Path) -> list[str]:
    """Build but never execute the future command; live relay stays locked."""
    config = relay.config_for(role)
    del config["sandbox_mode"]
    command = relay.codex_command(config, workspace / "solution")
    command[0] = str(cli.resolve(strict=True))
    return command[:-1] + permissions(role, workspace, cli) + ["-"]


def capture_process(argv: list[str], prompt: str, capture: Path, *, cwd: Path,
                    timeout: float | None = None) -> dict:
    """Drain stdout/stderr directly to exclusive private files, without shell.

    No retries, decoding, truncation or secret filtering of private evidence.
    timeout is for bounded infrastructure probes, not a candidate token budget.
    On interruption terminate the process group, retain partial files and raise.
    Parent SIGKILL/power failure cannot guarantee a final checkpoint.
    """
    if capture.exists() or capture.is_symlink():
        raise FileExistsError("Capture must be new")
    capture.mkdir(mode=0o700)
    started = time.monotonic()
    process = None
    state = {"status": "starting", "exit_code": None}
    relay.save(capture / "process.json", state)
    try:
        # A file for stdin avoids pipe deadlock on large prompts/output.
        with (capture / "prompt.txt").open("x+b") as source, \
                (capture / "stdout.jsonl").open("xb") as out, \
                (capture / "stderr.txt").open("xb") as err:
            source.write(prompt.encode("utf-8"))
            source.seek(0)
            process = subprocess.Popen(argv, stdin=source, stdout=out, stderr=err,
                                       cwd=cwd, start_new_session=True)
            state.update(status="running", pid=process.pid)
            relay.save(capture / "process.json", state)
            state["exit_code"] = process.wait(timeout=timeout)
            state["status"] = "completed" if process.returncode == 0 else "failed"
    except BaseException as error:
        state.update(status="interrupted", error_type=type(error).__name__)
        raise
    finally:
        if process is not None:
            # Also kill descendants left behind by a normally exited parent.
            try:
                os.killpg(process.pid, signal.SIGKILL)
            except ProcessLookupError:
                pass
            process.wait()
            state["exit_code"] = process.returncode
        state["duration_seconds"] = time.monotonic() - started
        relay.save(capture / "process.json", state)
    return state


def local_cli() -> Path:
    path = shutil.which("codex")
    if path is None:
        raise FileNotFoundError("Codex CLI is unavailable")
    return Path(path).resolve(strict=True)


def isolated_command(role: str, workspace: Path, argv: list[str]) -> list[str]:
    """Local process fixture isolation, NOT a wrapper for authenticated Codex.

    Host credentials and home are deliberately absent. Read-only synthetic root
    also prevents writes into the otherwise writable namespace skeleton.
    """
    if role not in {"MAIN", "REV-01"} or workspace.is_symlink():
        raise ValueError("Invalid role/workspace")
    workspace = workspace.resolve(strict=True)
    solution = workspace / "solution"
    if solution.is_symlink() or not solution.is_dir():
        raise ValueError("Invalid solution")
    command = ["/usr/bin/bwrap", "--die-with-parent", "--unshare-user",
               "--unshare-pid", "--unshare-net", "--unshare-ipc", "--unshare-uts",
               "--clearenv", "--setenv", "PATH", "/usr/bin:/bin",
               "--setenv", "PYTHONDONTWRITEBYTECODE", "1"]
    for path in ("/usr", "/bin", "/lib", "/lib64"):
        if Path(path).exists():
            command += ["--ro-bind", path, path]
    command += ["--proc", "/proc", "--dev", "/dev",
                "--ro-bind", str(workspace), str(workspace)]
    if role == "MAIN":
        command += ["--bind", str(solution), str(solution)]
    return command + ["--remount-ro", "/", "--chdir", str(solution), "--", *argv]
