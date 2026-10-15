#!/usr/bin/env python3
"""One explicitly authorised lean Core attempt. No retry, no scientific run."""
import argparse
import json
from pathlib import Path

import run_v2_2_lean as lean
from run_v2_2_supervised import command
from v2_2_transport import capture_process

RUN_ID = "astra-medium-core-v2-2-lean-001"
MANIFEST = lean.relay.ROOT / "governance/v2-2-lean-001.json"


def validate():
    manifest = json.loads(MANIFEST.read_text())
    expected = {"run_id": RUN_ID, "protocol_frozen": True, "launch_authorized": True,
                "challenge": "calculator", "model": "gpt-6-astra", "reasoning_effort": "medium",
                "max_sessions": 3, "payload_character_cap": 12000, "target_tokens": 100000,
                "between_session_token_stop": 150000, "hard_token_cap": None,
                "retry_authorized": False, "scientific_authorized": False,
                "final_word_limits": [150, 300, 300]}
    if any(type(manifest.get(k)) is not type(v) or manifest[k] != v for k, v in expected.items()):
        raise PermissionError("Unauthorised attempt or altered conditions")
    if manifest["mandates"] != ["v2-2-lean-001-initial.md", "v2-2-lean-001-review.md", "v2-2-lean-001-final.md"]:
        raise ValueError("Unexpected mandates")
    for path, expected_hash in manifest["inputs_sha256"].items():
        if lean.relay.digest((lean.relay.ROOT / path).read_bytes()) != expected_hash:
            raise ValueError("Frozen input changed: " + path)
    return manifest


def transport(request, capture=capture_process):
    """Use the existing native CLI permissions and private subprocess capture."""
    process = capture(command(request["config"], request["cwd"]), request["prompt"],
                      request["capture"] / "process", cwd=request["cwd"])
    return {"exit_code": process["exit_code"], "process": process,
            "jsonl": (request["capture"] / "process/stdout.jsonl").read_text()}


def launch(root):
    manifest = validate()
    root = Path(root).resolve()
    if root.exists() or root.is_relative_to(lean.relay.ROOT) or lean.relay.ROOT.is_relative_to(root):
        raise ValueError("Fresh external workspace required")
    public = lean.relay.ROOT / "runs" / RUN_ID
    public.mkdir()  # Persistent one-shot reservation, including failed launches.
    (public / "CHALLENGE.md").write_bytes((lean.relay.ROOT / "challenges/calculator/SPEC.md").read_bytes())
    lean.relay.save(public / "run.json", {"run_id": RUN_ID, "status": "reserved",
                    "campaign": manifest["campaign"], "exploratory": True})
    return lean.run_engine(root, manifest, transport, simulation=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--run", type=Path)
    args = parser.parse_args()
    if args.check == (args.run is not None):
        parser.error("Choose --check or --run NEW_EXTERNAL_DIRECTORY")
    if args.check:
        validate()
        print("Frozen inputs verified; no model called")
    else:
        state = launch(args.run)
        print(json.dumps({k: state[k] for k in ("status", "known_tokens", "usage_complete", "wall_duration_seconds")}))
