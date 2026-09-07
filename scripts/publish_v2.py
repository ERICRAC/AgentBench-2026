#!/usr/bin/env python3
"""Publish screened V2 messages and observable events from a private capture."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
SESSION_META = {
    "sa01_initial": ("MSG-001", "RELAY → SA-01 → MAIN", "analyse indépendante", 1200),
    "sa02_initial": ("MSG-002", "RELAY → SA-02 → MAIN", "analyse indépendante", 1200),
    "sa01_cross": ("MSG-003", "MAIN/RELAY → SA-01 → MAIN", "contradiction croisée", 600),
    "sa02_cross": ("MSG-004", "MAIN/RELAY → SA-02 → MAIN", "contradiction croisée", 600),
    "main_first": ("MSG-005", "RELAY → MAIN", "arbitrage et première solution", None),
    "sa03_critic": ("MSG-006", "MAIN/RELAY → SA-03 → MAIN", "critique adversariale", 1200),
    "main_final": ("MSG-007", "RELAY → MAIN", "arbitrage final et vérification", None),
}
SECRET_PATTERNS = (
    re.compile(r"sk-[A-Za-z0-9_-]{20,}"),
    re.compile(r"ghp_[A-Za-z0-9]{20,}"),
    re.compile(r"github_pat_[A-Za-z0-9_]{20,}"),
    re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
)


def screen(text: str) -> str:
    screened = text.replace(str(ROOT), "<repo>")
    for pattern in SECRET_PATTERNS:
        screened = pattern.sub("<redacted-secret>", screened)
    return screened


def code_block(text: str) -> str:
    return f"````text\n{screen(text).rstrip()}\n````\n"


def usage_total(record: dict[str, object]) -> int:
    usage = record.get("usage") or {}
    return int(usage.get("input_tokens", 0)) + int(usage.get("output_tokens", 0))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--private-record", required=True, type=Path)
    parser.add_argument("--run", required=True, type=Path)
    args = parser.parse_args()

    private_record = args.private_record.resolve()
    private_root = private_record.parent
    run_dir = args.run.resolve()
    data = json.loads(private_record.read_text(encoding="utf-8"))
    if data["run_id"] != run_dir.name:
        parser.error("Private record and run directory do not match")

    records = data["records"]
    total_input = sum(int((record.get("usage") or {}).get("input_tokens", 0)) for record in records.values())
    total_cache = sum(int((record.get("usage") or {}).get("cached_input_tokens", 0)) for record in records.values())
    total_output = sum(int((record.get("usage") or {}).get("output_tokens", 0)) for record in records.values())
    total_reasoning = sum(int((record.get("usage") or {}).get("reasoning_output_tokens", 0)) for record in records.values())
    session_seconds = sum(float(record["duration_seconds"]) for record in records.values())

    lines = [
        f"# PV multi-agent — {run_dir.name}",
        "",
        "## Identification et périmètre",
        "",
        "Le commanditaire lance V2 Sol/high. L'orchestrateur expérimental",
        "exécute le relais mécanique et publie après clôture. MAIN est le seul",
        "rôle écrivain. SA-01, SA-02 et SA-03 sont consultants en lecture seule,",
        "sans sous-délégation. Les sept sessions sont neuves et éphémères.",
        "",
        "Les textes ci-dessous sont conservés dans l'ordre des phases. Seuls le",
        "préfixe local du dépôt et d'éventuels secrets reconnus sont remplacés ;",
        "aucun raisonnement interne n'est publié.",
        "",
        "## Équipe et métriques",
        "",
        "| Session | Rôle / phase | Durée | Entrée | Cache inclus | Sortie | Raisonnement inclus | Mots visibles |",
        "| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for name, record in records.items():
        message_id, _, phase, limit = SESSION_META[name]
        usage = record.get("usage") or {}
        word_count = sum(len(message.split()) for message in record["visible_messages"])
        label = f"{message_id} · {phase}"
        if limit is not None:
            label += f" (max {limit})"
        lines.append(
            f"| {record['label']} | {label} | {record['duration_seconds']} s | "
            f"{usage.get('input_tokens', 0)} | {usage.get('cached_input_tokens', 0)} | "
            f"{usage.get('output_tokens', 0)} | {usage.get('reasoning_output_tokens', 0)} | "
            f"{word_count} |"
        )
    lines.extend(
        [
            "",
            f"Temps mural : **{data['wall_duration_seconds']} s**. Somme des temps-sessions : "
            f"**{session_seconds:.3f} s**.",
            "",
            f"Tokens : **{total_input} entrée + {total_output} sortie = "
            f"{total_input + total_output}**. Le cache ({total_cache}) est inclus dans",
            f"l'entrée et le raisonnement ({total_reasoning}) dans la sortie.",
            "",
            "## Messages visibles — verbatim filtré",
            "",
        ]
    )

    for name, record in records.items():
        message_id, direction, phase, limit = SESSION_META[name]
        word_count = sum(len(message.split()) for message in record["visible_messages"])
        prompt_path = private_root / record["label"] / "prompt.txt"
        prompt = prompt_path.read_text(encoding="utf-8")
        reply = "\n\n".join(record["visible_messages"])
        lines.extend(
            [
                f"### {message_id} — {phase}",
                "",
                f"Direction : `{direction}`. Réponse visible : {word_count} mots"
                + (f" sur {limit} maximum." if limit is not None else "."),
                "",
                "<details>",
                "<summary>Texte envoyé, mot pour mot</summary>",
                "",
                code_block(prompt).rstrip(),
                "",
                "</details>",
                "",
                f"#### Texte retourné pour {message_id}, mot pour mot",
                "",
                code_block(reply).rstrip(),
                "",
            ]
        )

    lines.extend(
        [
            "## Lecture sociale synthétique",
            "",
            "SA-01 et SA-02 commencent sans voir l'avis de l'autre. Leurs réponses",
            "croisées rendent ensuite visibles accords, désaccords et doublons. MAIN",
            "arbitre avant d'écrire. SA-03 critique l'instantané obtenu ; MAIN qualifie",
            "alors chaque point avant le vérificateur. Le rapport de résultat chiffre",
            "les recommandations retenues, écartées et non vérifiables.",
            "",
            "Les prompts dynamiques répètent volontairement le challenge et les textes",
            "antérieurs : cette duplication fait partie du coût de coordination mesuré.",
            "",
        ]
    )
    (run_dir / "PV.md").write_text("\n".join(lines), encoding="utf-8")

    sessions = []
    for name, record in records.items():
        public_events = json.loads(screen(json.dumps(record["events"], ensure_ascii=False)))
        sessions.append(
            {
                "phase": name,
                "label": record["label"],
                "thread_id": record["thread_id"],
                "config_file": record["config_file"],
                "config_sha256": record["config_sha256"],
                "prompt_sha256": record["prompt_sha256"],
                "duration_seconds": record["duration_seconds"],
                "usage": record["usage"],
                "exit_code": record["exit_code"],
                "events": public_events,
                "errors": record["errors"],
            }
        )
    trace = {
        "run_id": data["run_id"],
        "note": "Observable agent messages, commands and file changes only; internal reasoning excluded. Full screened prompts and replies are in PV.md.",
        "wall_duration_seconds": data["wall_duration_seconds"],
        "sessions": sessions,
    }
    (run_dir / "trace.json").write_text(
        json.dumps(trace, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "run_id": data["run_id"],
                "wall_duration_seconds": data["wall_duration_seconds"],
                "sum_session_seconds": round(session_seconds, 3),
                "input_tokens": total_input,
                "cached_input_tokens": total_cache,
                "output_tokens": total_output,
                "reasoning_output_tokens": total_reasoning,
                "input_plus_output_tokens": total_input + total_output,
            }
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
