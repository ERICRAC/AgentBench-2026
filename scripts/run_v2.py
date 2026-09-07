#!/usr/bin/env python3
"""Run the frozen V2 social sequence while keeping raw captures private."""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
import os
from pathlib import Path
import subprocess
import tempfile
import time
import tomllib


ROOT = Path(__file__).resolve().parents[1]
ROLES = ("MAIN", "SA-01", "SA-02", "SA-03")


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def read_config(path: Path) -> tuple[bytes, dict[str, object]]:
    raw = path.read_bytes()
    config = tomllib.loads(raw.decode("utf-8"))
    if any(not isinstance(value, (str, int, bool)) for value in config.values()):
        raise ValueError(f"Only scalar TOML values are supported: {path}")
    return raw, config


def run_session(
    *,
    label: str,
    config_path: Path,
    prompt: str,
    cwd: Path,
    private_root: Path,
) -> dict[str, object]:
    config_raw, config = read_config(config_path)
    command = [
        "codex",
        "exec",
        "--strict-config",
        "--ignore-user-config",
        "--ignore-rules",
        "--ephemeral",
        "--json",
        "--skip-git-repo-check",
        "-C",
        str(cwd.resolve()),
    ]
    for key, value in config.items():
        command.extend(["-c", f"{key}={json.dumps(value)}"])
    command.append("-")

    session_dir = private_root / label
    session_dir.mkdir()
    (session_dir / "prompt.txt").write_text(prompt, encoding="utf-8")
    started = time.monotonic()
    environment = os.environ.copy()
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    with (session_dir / "events.jsonl").open("w", encoding="utf-8") as output:
        with (session_dir / "stderr.txt").open("w", encoding="utf-8") as error:
            completed = subprocess.run(
                command,
                input=prompt,
                text=True,
                stdout=output,
                stderr=error,
                env=environment,
                check=False,
            )

    record: dict[str, object] = {
        "label": label,
        "config_file": str(config_path.relative_to(ROOT)),
        "config": config,
        "config_sha256": sha256(config_raw),
        "prompt_sha256": sha256(prompt.encode("utf-8")),
        "duration_seconds": round(time.monotonic() - started, 3),
        "exit_code": completed.returncode,
        "thread_id": None,
        "usage": None,
        "visible_messages": [],
        "events": [],
        "errors": [],
    }
    for line in (session_dir / "events.jsonl").read_text(encoding="utf-8").splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        event_type = event.get("type")
        if event_type == "thread.started":
            record["thread_id"] = event.get("thread_id")
        elif event_type == "turn.completed":
            record["usage"] = event.get("usage")
        elif event_type in {"error", "turn.failed"}:
            record["errors"].append(event)
        elif event_type == "item.completed":
            item = event.get("item", {})
            item_type = item.get("type")
            if item_type == "agent_message":
                record["visible_messages"].append(item.get("text", ""))
            if item_type in {"agent_message", "command_execution", "file_change"}:
                public_item = {"type": item_type}
                for key in ("text", "command", "exit_code", "changes"):
                    if key in item:
                        public_item[key] = item[key]
                record["events"].append(public_item)
    (session_dir / "record.json").write_text(
        json.dumps(record, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    if completed.returncode != 0 or record["errors"] or not record["visible_messages"]:
        raise RuntimeError(f"Session {label} failed; inspect {session_dir}")
    return record


def visible_text(record: dict[str, object]) -> str:
    messages = record["visible_messages"]
    assert isinstance(messages, list)
    return "\n\n".join(str(message) for message in messages)


def block(name: str, text: str) -> str:
    return f"\n--- BEGIN {name} ---\n{text}\n--- END {name} ---\n"


def snapshot_solution(solution: Path) -> str:
    chunks: list[str] = []
    for path in sorted(item for item in solution.rglob("*") if item.is_file()):
        if "__pycache__" in path.parts or path.suffix == ".pyc":
            continue
        relative = path.relative_to(solution)
        chunks.append(block(f"FILE solution/{relative}", path.read_text(encoding="utf-8")))
    return "".join(chunks)


def initial_prompt(role: str, mission: str, challenge: str) -> str:
    return (
        f"AgentBench V2. Tu es {role}. {mission}\n"
        "Analyse indépendamment le challenge ci-dessous en 1 200 mots maximum. "
        "Tu es consultant en lecture seule : n'utilise aucun outil, ne délègue "
        "rien, ne consulte aucun dépôt et ne fournis qu'un avis visible. Structure "
        "les recommandations pour permettre un arbitrage explicite."
        + block("CHALLENGE", challenge)
    )


def contradiction_prompt(
    role: str,
    mission: str,
    own: str,
    peer_role: str,
    peer: str,
) -> str:
    return (
        f"AgentBench V2. Tu es {role}. {mission}\n"
        "Voici mot pour mot ton avis initial et celui de l'autre consultant. "
        "Produis une seule contradiction, confirmation ou révision de 600 mots "
        "maximum. Identifie accords, désaccords utiles, doublons et priorité des "
        "recommandations. N'utilise aucun outil et ne délègue rien."
        + block(f"YOUR INITIAL {role}", own)
        + block(f"PEER INITIAL {peer_role}", peer)
    )


def main_first_prompt(
    challenge: str,
    base_prompt: str,
    records: dict[str, dict[str, object]],
) -> str:
    return (
        "AgentBench V2 — phase MAIN première solution. Tu es l'orchestrateur "
        "candidat et l'unique écrivain. L'orchestrateur expérimental a déjà "
        "exécuté exactement les consultants SA-01 et SA-02 selon le protocole ; "
        "ne lance aucun autre agent. Lis leurs quatre textes comme des avis non "
        "contraignants. Avant de coder, crée `solution/DECISIONS.md` avec une table "
        "reliant chaque recommandation à une décision motivée. Implémente ensuite "
        "une première solution complète et documentée, uniquement dans `solution/`. "
        "Tu peux effectuer des contrôles ciblés, mais ne lance pas encore le "
        "vérificateur officiel : la critique SA-03 doit examiner cette première "
        "solution. Ne fais aucune opération Git. Termine par une synthèse visible."
        + block("BASE MULTI-AGENT PROMPT", base_prompt)
        + block("CHALLENGE", challenge)
        + block("SA-01 INITIAL", visible_text(records["sa01_initial"]))
        + block("SA-02 INITIAL", visible_text(records["sa02_initial"]))
        + block("SA-01 CONTRADICTION", visible_text(records["sa01_cross"]))
        + block("SA-02 CONTRADICTION", visible_text(records["sa02_cross"]))
    )


def critic_prompt(challenge: str, consultations: str, solution: str) -> str:
    return (
        "AgentBench V2. Tu es SA-03, critique QA adversarial en lecture seule. "
        "Examine le challenge, les avis transmis, la table de décisions et la "
        "première solution ci-dessous. En 1 200 mots maximum, cherche omissions, "
        "failles de sécurité, erreurs de contrat, cas limites et régressions. "
        "Distingue défaut confirmé, risque et préférence. N'utilise aucun outil, "
        "ne délègue rien et ne réécris pas la solution."
        + block("CHALLENGE", challenge)
        + block("CONSULTATIONS", consultations)
        + block("FIRST SOLUTION", solution)
    )


def main_final_prompt(
    challenge: str,
    base_prompt: str,
    consultations: str,
    first_solution: str,
    critic: str,
    verifier_command: str,
) -> str:
    return (
        "AgentBench V2 — phase MAIN finale. Tu représentes le même rôle MAIN, "
        "orchestrateur candidat et unique écrivain, dans une nouvelle session "
        "éphémère mesurée. Aucun nouveau consultant n'est autorisé. Reprends la "
        "première solution présente dans `solution/`. Qualifie chaque point de "
        "SA-03 comme retenu, écarté ou non vérifiable et complète "
        "`solution/DECISIONS.md` avec la justification et la preuve. Applique "
        "uniquement les corrections retenues. Exécute ensuite le vérificateur "
        f"officiel exactement ainsi : `{verifier_command}`. Corrige les défauts "
        "confirmés jusqu'au verdict final. Écris uniquement dans `solution/`, "
        "n'effectue aucune opération Git et restitue rôles, arbitrages, premier "
        "passage, verdict final, corrections et limites."
        + block("BASE MULTI-AGENT PROMPT", base_prompt)
        + block("CHALLENGE", challenge)
        + block("CONSULTATIONS", consultations)
        + block("FIRST SOLUTION SNAPSHOT", first_solution)
        + block("SA-03 CRITIQUE", critic)
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Execute one AgentBench V2 run.")
    parser.add_argument("--run", required=True, type=Path)
    parser.add_argument(
        "--challenge",
        choices=("calculator", "scientific-calculator"),
        default="calculator",
    )
    args = parser.parse_args()

    run_dir = args.run.resolve()
    solution = run_dir / "solution"
    challenge_path = run_dir / "CHALLENGE.md"
    if not solution.is_dir() or not challenge_path.is_file():
        parser.error("Run must contain solution/ and CHALLENGE.md")
    if any(solution.iterdir()):
        parser.error("V2 solution directory must be empty before launch")

    configs = {role: run_dir / f"config-{role.lower()}.toml" for role in ROLES}
    missing = [str(path) for path in configs.values() if not path.is_file()]
    if missing:
        parser.error(f"Missing role configurations: {missing}")

    challenge = challenge_path.read_text(encoding="utf-8")
    base_prompt = (ROOT / "prompts" / "codex-multi.md").read_text(encoding="utf-8")
    private_root = Path(tempfile.mkdtemp(prefix=f"agentbench-{run_dir.name}-"))
    print(f"Private V2 capture: {private_root}", flush=True)
    wall_started = time.monotonic()

    missions = {
        "SA-01": "Analyste exigences et sécurité : obligations, ambiguïtés, erreurs et surfaces d'attaque.",
        "SA-02": "Architecte logiciel et testabilité : structure, invariants, stratégie de validation et cas sensibles.",
    }
    with ThreadPoolExecutor(max_workers=2) as executor:
        futures = {
            "sa01_initial": executor.submit(
                run_session,
                label="01-sa01-initial",
                config_path=configs["SA-01"],
                prompt=initial_prompt("SA-01", missions["SA-01"], challenge),
                cwd=solution,
                private_root=private_root,
            ),
            "sa02_initial": executor.submit(
                run_session,
                label="02-sa02-initial",
                config_path=configs["SA-02"],
                prompt=initial_prompt("SA-02", missions["SA-02"], challenge),
                cwd=solution,
                private_root=private_root,
            ),
        }
        records = {name: future.result() for name, future in futures.items()}

    with ThreadPoolExecutor(max_workers=2) as executor:
        futures = {
            "sa01_cross": executor.submit(
                run_session,
                label="03-sa01-cross",
                config_path=configs["SA-01"],
                prompt=contradiction_prompt(
                    "SA-01",
                    missions["SA-01"],
                    visible_text(records["sa01_initial"]),
                    "SA-02",
                    visible_text(records["sa02_initial"]),
                ),
                cwd=solution,
                private_root=private_root,
            ),
            "sa02_cross": executor.submit(
                run_session,
                label="04-sa02-cross",
                config_path=configs["SA-02"],
                prompt=contradiction_prompt(
                    "SA-02",
                    missions["SA-02"],
                    visible_text(records["sa02_initial"]),
                    "SA-01",
                    visible_text(records["sa01_initial"]),
                ),
                cwd=solution,
                private_root=private_root,
            ),
        }
        records.update({name: future.result() for name, future in futures.items()})

    records["main_first"] = run_session(
        label="05-main-first",
        config_path=configs["MAIN"],
        prompt=main_first_prompt(challenge, base_prompt, records),
        cwd=solution,
        private_root=private_root,
    )
    first_solution = snapshot_solution(solution)
    consultation_text = "".join(
        block(name.upper(), visible_text(records[name]))
        for name in ("sa01_initial", "sa02_initial", "sa01_cross", "sa02_cross")
    )
    records["sa03_critic"] = run_session(
        label="06-sa03-critic",
        config_path=configs["SA-03"],
        prompt=critic_prompt(challenge, consultation_text, first_solution),
        cwd=solution,
        private_root=private_root,
    )

    verifier = "python3 scripts/verify.py --solution " + str(solution.relative_to(ROOT))
    if args.challenge == "scientific-calculator":
        verifier = (
            "python3 scripts/verify.py --challenge scientific-calculator --solution "
            + str(solution.relative_to(ROOT))
        )
    records["main_final"] = run_session(
        label="07-main-final",
        config_path=configs["MAIN"],
        prompt=main_final_prompt(
            challenge,
            base_prompt,
            consultation_text,
            first_solution,
            visible_text(records["sa03_critic"]),
            verifier,
        ),
        cwd=solution,
        private_root=private_root,
    )

    summary = {
        "run_id": run_dir.name,
        "challenge": args.challenge,
        "codex_cli": subprocess.check_output(["codex", "--version"], text=True).strip(),
        "wall_duration_seconds": round(time.monotonic() - wall_started, 3),
        "records": records,
    }
    (private_root / "v2-record.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "run_id": run_dir.name,
                "wall_duration_seconds": summary["wall_duration_seconds"],
                "sessions": {
                    name: {
                        "thread_id": record["thread_id"],
                        "duration_seconds": record["duration_seconds"],
                        "usage": record["usage"],
                    }
                    for name, record in records.items()
                },
            },
            ensure_ascii=False,
        ),
        flush=True,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
