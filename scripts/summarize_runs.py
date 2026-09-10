#!/usr/bin/env python3
"""Generate editorial entry pages from public evidence, never rewrite runs/.

Facts come from run.json and trace.json. Editorial interpretation is separately
maintained in docs/run-interpretations.json. Missing counters remain missing.
The renderer accepts arbitrary roles and sessions; only the legacy V2 topology
adapter knows the seven-session protocol. No message body is copied here.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from observe_sessions import v2_topology

ROOT = Path(__file__).resolve().parents[1]
LANGS = {"fr": "", "en": ".en", "es": ".es", "pt": ".pt"}
NAMES = {"fr": "Français", "en": "English (UK)", "es": "Español", "pt": "Português"}
UI = {
    "fr": ["Le run en 2 minutes", "Faits observés", "Équipe et chronologie", "Analyse interprétative", "Preuves et suite", "Non enregistré", "Premier passage officiel", "Verdict indépendant", "Temps mural (s)", "Tokens entrée + sortie", "Sessions enregistrées (pas appels API)", "Session", "Rôle", "Groupe parallèle spécifié", "Durée CLI (s)", "Début / fin mesurés (s)", "Dépend de", "Modèle / effort", "Synthèses des runs V2", "Résumés générés ; preuves historiques inchangées.", "Guide de lecture", "Décisions", "Tests", "Conclusions", "Calculatrice simple", "Calculatrice scientifique", "Écrivain", "Oui", "Non", "MAIN : arbitre et seul écrivain ; SA-01 : exigences/sécurité ; SA-02 : architecture/testabilité ; SA-03 : relecture critique. RELAY est le superviseur mécanique externe, pas un candidat.", "P1 : analyses indépendantes, puis barrière. P2 : revues croisées, puis barrière. Ensuite MAIN → SA-03 → MAIN et vérificateur. Le parallélisme historique est spécifié, pas un chevauchement mesuré.", "Le cache est inclus dans l’entrée ; le raisonnement est inclus dans la sortie. Ne pas les additionner de nouveau. Une session CLI peut contenir plusieurs appels modèle. Le premier passage officiel vient après la critique, pas avant.", "Cette couche précède le PV détaillé dans le parcours de lecture ; le PV original reste inchangé. Les cellules absentes ne valent pas zéro.", "Corrections fonctionnelles après premier passage", "Résultat candidat final", "Durée d’invocation mesurée (s)", "Les mesures d’invocation ont une origine distincte du temps mural historique ; voir le guide d’instrumentation."],
    "en": ["The run in 2 minutes", "Observed facts", "Team and sequence", "Interpretative analysis", "Evidence and next steps", "Not recorded", "First official pass", "Independent verdict", "Wall duration (s)", "Input + output tokens", "Recorded sessions (not API calls)", "Session", "Role", "Specified parallel group", "CLI duration (s)", "Measured start / end (s)", "Depends on", "Model / effort", "V2 run summaries", "Generated summaries; historical evidence unchanged.", "Reading guide", "Decisions", "Tests", "Conclusions", "Simple calculator", "Scientific calculator", "Writer", "Yes", "No", "MAIN: arbiter and sole writer; SA-01: requirements/security; SA-02: architecture/testability; SA-03: critical reviewer. RELAY is the external mechanical supervisor, not a candidate.", "P1: independent analyses, then a barrier. P2: cross-reviews, then a barrier. Next MAIN → SA-03 → MAIN and verifier. Historical parallelism is specified, not measured overlap.", "Cache is included in input; reasoning is included in output. Do not add them again. A CLI session may contain several model calls. The first official pass follows the critique, not the other way round.", "This layer precedes the detailed minutes in the reading journey; the original minutes remain unchanged. Missing cells do not mean zero.", "Functional corrections after first pass", "Final candidate result", "Measured invocation duration (s)", "Invocation measurements have a different origin from historical wall duration; see the instrumentation guide."],
    "es": ["El run en 2 minutos", "Hechos observados", "Equipo y secuencia", "Análisis interpretativo", "Pruebas y próximos pasos", "No registrado", "Primera verificación oficial", "Veredicto independiente", "Duración total (s)", "Tokens entrada + salida", "Sesiones registradas (no llamadas API)", "Sesión", "Rol", "Grupo paralelo especificado", "Duración CLI (s)", "Inicio / fin medidos (s)", "Depende de", "Modelo / esfuerzo", "Resúmenes de runs V2", "Resúmenes generados; pruebas históricas intactas.", "Guía de lectura", "Decisiones", "Tests", "Conclusiones", "Calculadora simple", "Calculadora científica", "Escritor", "Sí", "No", "MAIN: árbitro y único escritor; SA-01: requisitos/seguridad; SA-02: arquitectura/testabilidad; SA-03: revisión crítica. RELAY es el supervisor mecánico externo, no un candidato.", "P1: análisis independientes y barrera. P2: revisiones cruzadas y barrera. Después MAIN → SA-03 → MAIN y verificador. El paralelismo histórico está especificado, no es solapamiento medido.", "La caché está incluida en la entrada; el razonamiento, en la salida. No sumarlos otra vez. Una sesión CLI puede contener varias llamadas al modelo. La primera verificación oficial ocurre después de la crítica.", "Esta capa precede al acta detallada en la lectura; el acta original no cambia. Los datos ausentes no equivalen a cero.", "Correcciones funcionales después del primer pase", "Resultado final del candidato", "Duración de invocación medida (s)", "Las invocaciones tienen un origen distinto de la duración total histórica; véase la guía de instrumentación."],
    "pt": ["O run em 2 minutos", "Factos observados", "Equipa e sequência", "Análise interpretativa", "Provas e próximos passos", "Não registado", "Primeira verificação oficial", "Veredicto independente", "Duração total (s)", "Tokens entrada + saída", "Sessões registadas (não chamadas API)", "Sessão", "Papel", "Grupo paralelo especificado", "Duração CLI (s)", "Início / fim medidos (s)", "Depende de", "Modelo / esforço", "Resumos dos runs V2", "Resumos gerados; provas históricas intactas.", "Guia de leitura", "Decisões", "Testes", "Conclusões", "Calculadora simples", "Calculadora científica", "Escritor", "Sim", "Não", "MAIN: árbitro e único escritor; SA-01: requisitos/segurança; SA-02: arquitetura/testabilidade; SA-03: revisão crítica. RELAY é o supervisor mecânico externo, não um candidato.", "P1: análises independentes e barreira. P2: revisões cruzadas e barreira. Depois MAIN → SA-03 → MAIN e verificador. O paralelismo histórico está especificado, não é sobreposição medida.", "A cache está incluída na entrada; o raciocínio, na saída. Não somar novamente. Uma sessão CLI pode conter várias chamadas ao modelo. A primeira verificação oficial ocorre após a crítica.", "Esta camada precede a ata detalhada na leitura; a ata original não muda. Dados ausentes não significam zero.", "Correções funcionais após a primeira passagem", "Resultado final do candidato", "Duração de invocação medida (s)", "As invocações têm uma origem distinta da duração total histórica; ver o guia de instrumentação."],
}


def navigation(stem, language):
    return " · ".join(f"**{NAMES[lang]}**" if lang == language else
                      f"[{NAMES[lang]}]({stem}{suffix}.md)" for lang, suffix in LANGS.items())


def cell(value, missing):
    if value is None:
        return missing
    if isinstance(value, float):
        return f"{value:.3f}"
    return str(value).replace("|", "\\|").replace("\n", " ")


def render(data, trace, interpretation, language):
    t, suffix = UI[language], LANGS[language]
    run_id = data["run_id"]
    if trace.get("run_id", run_id) != run_id:
        raise ValueError("Metadata and trace identify different runs")
    evidence = f"../../runs/{run_id}"
    sessions = trace.get("sessions", [])
    verification = data.get("verification", {})
    usage = data.get("usage") or {}
    tokens = usage.get("input_plus_output_tokens")
    if tokens is None and all(usage.get(key) is not None for key in ("input_tokens", "output_tokens")):
        tokens = usage["input_tokens"] + usage["output_tokens"]
    rows = [(t[17], f"{data.get('candidate_model', t[5])} / {data.get('reasoning_effort', t[5])}"),
            (t[6], verification.get("candidate_first_official_pass")),
            (t[34], verification.get("candidate_final_pass")),
            (t[7], verification.get("independent_final_pass")),
            (t[8], data.get("wall_duration_seconds")), (t[9], tokens),
            (t[10], len(sessions) if "sessions" in trace else None),
            (t[33], verification.get("functional_corrections_after_first_official_pass"))]
    challenge = {"calculator": t[24], "scientific-calculator": t[25]}.get(
        data.get("challenge"), data.get("challenge", t[5]))
    lines = [f"# {t[0]} — {run_id}", "", navigation(run_id, language), "", t[32], "",
             f"{challenge} · {data.get('mode', t[5])} · {data.get('status', t[5])}",
             "", f"## {t[1]}", "", "| | |", "| --- | --- |"]
    lines += [f"| {label} | {cell(value, t[5])} |" for label, value in rows]
    legacy = data.get("mode") == "codex-multi" and data.get("runner_sha256") == "3cb0f940ebc8fe0c422b948c35de4b00273815d3dc4cb91f04b53e62814f19c4"
    # The last sentence describes frozen V2 ordering, not arbitrary topologies.
    costs_note = t[31] if legacy else t[31].rsplit(". ", 1)[0] + "."
    lines += ["", costs_note, "", f"## {t[2]}", ""]
    topology = {e["session_id"]: e for e in v2_topology().values()} if legacy else {}
    if legacy:
        lines += [t[29], "", t[30], ""]
    else:
        for role, description in trace.get("roles", {}).items():
            lines += [f"- {cell(role, t[5])}: {cell(description, t[5])}"]
        lines += [""]
    lines += ["<details>", f"<summary>{t[10]}</summary>", "",
              f"| {t[11]} | {t[12]} | {t[13]} | {t[16]} | receives_from | {t[26]} | {t[14]} | {t[9]} | {t[15]} | {t[35]} |",
              "| --- | --- | --- | --- | --- | --- | ---: | ---: | --- | ---: |"]
    for session in sessions:
        phase = session.get("session_id", session.get("phase"))
        observation = session.get("observation") or {}
        specified = observation or topology.get(phase, {})
        interval = (f"{observation['started_at_seconds']:.3f} / {observation['ended_at_seconds']:.3f}"
                    if observation else None)
        counters = session.get("usage") or {}
        token_count = (counters["input_tokens"] + counters["output_tokens"]
                       if all(counters.get(k) is not None for k in ("input_tokens", "output_tokens")) else None)
        writer = specified.get("writes_solution")
        values = [phase, session.get("role"), (specified["parallel_group"] or "—") if "parallel_group" in specified else None,
                  ", ".join(specified["depends_on"]) or "—" if "depends_on" in specified else None,
                  ", ".join(specified["receives_from"]) or "—" if "receives_from" in specified else None,
                  t[27] if writer is True else t[28] if writer is False else None,
                  session.get("duration_seconds"), token_count, interval,
                  observation.get("duration_seconds")]
        lines.append("| " + " | ".join(cell(v, t[5]) for v in values) + " |")
    trace_link = "../../" + data.get("trace", f"runs/{run_id}/trace.json")
    lines += ["", t[36], "", "</details>", "", f"## {t[3]}", "", interpretation, "",
              f"## {t[4]}", "",
              f"[PV / verbatim]({evidence}/PV.md) · [trace.json]({trace_link}) · [run.json]({evidence}/run.json) · [{t[21]}]({evidence}/solution/DECISIONS.md)", "",
              f"[{t[20]}](../../docs/reading-guide{suffix}.md) · [{t[22]}](../../docs/acceptance-tests{suffix}.md) · [{t[23]}](../CONCLUSIONS{suffix}.md) · [Index](index{suffix}.md)", ""]
    return "\n".join(lines)


def generate(check=False):
    annotations = json.loads((ROOT / "docs/run-interpretations.json").read_text())
    directory = ROOT / "results/run-summaries"
    if not check:
        directory.mkdir(exist_ok=True)
    stale = []
    for language, suffix in LANGS.items():
        index = [f"# {UI[language][18]}", "", navigation("index", language), "", UI[language][19], ""]
        for run_id, annotation in annotations.items():
            run_dir = ROOT / "runs" / run_id
            data = json.loads((run_dir / "run.json").read_text())
            trace = json.loads((run_dir / "trace.json").read_text())
            output = directory / f"{run_id}{suffix}.md"
            content = render(data, trace, annotation[language], language)
            if check:
                if not output.exists() or output.read_text() != content:
                    stale.append(str(output.relative_to(ROOT)))
            else:
                output.write_text(content, encoding="utf-8")
            index.append(f"- [{run_id}]({run_id}{suffix}.md)")
        index += ["", f"[{UI[language][20]}](../../docs/reading-guide{suffix}.md) · [{UI[language][23]}](../CONCLUSIONS{suffix}.md)", ""]
        output = directory / f"index{suffix}.md"
        content = "\n".join(index)
        if check:
            if not output.exists() or output.read_text() != content:
                stale.append(str(output.relative_to(ROOT)))
        else:
            output.write_text(content, encoding="utf-8")
    if stale:
        raise SystemExit("Stale generated pages: " + ", ".join(stale))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--run", type=Path, help="Future run with public run.json and trace.json")
    parser.add_argument("--interpretation", type=Path, help="Reviewed JSON with fr/en/es/pt editorial texts")
    args = parser.parse_args()
    if args.run is None:
        if args.interpretation:
            parser.error("--interpretation requires --run")
        generate(args.check)
    else:
        directory = args.run.resolve()
        if directory.parent != ROOT / "runs":
            parser.error("--run must be a direct child of runs/")
        data = json.loads((directory / "run.json").read_text())
        if data["run_id"] != directory.name:
            parser.error("run_id differs from directory")
        trace = json.loads((ROOT / data.get("trace", f"runs/{directory.name}/trace.json")).read_text())
        annotations = json.loads(args.interpretation.read_text()) if args.interpretation else {}
        destination = ROOT / "results/run-summaries"
        if not args.check:
            destination.mkdir(exist_ok=True)
        for language, suffix in LANGS.items():
            content = render(data, trace, annotations.get(language, UI[language][5]), language)
            output = destination / f"{directory.name}{suffix}.md"
            if args.check:
                if not output.exists() or output.read_text() != content:
                    raise SystemExit(f"Stale summary: {output}")
            else:
                output.write_text(content, encoding="utf-8")
