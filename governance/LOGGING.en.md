# Public logging policy

[Français](LOGGING.md) · **English (UK)** · [Español](LOGGING.es.md) · [Português](LOGGING.pt.md)

The log makes the process auditable without exposing complete conversations.
Each entry has a stable sequential number and no date or time.

## Retained content

- one-sentence restatement of the human request;
- summary of the agent's response or action;
- participating agent roles;
- decisions and rationale useful to the experiment;
- affected files and check results;
- material errors, corrections and human interventions;
- available metrics, qualified when approximate.

## Excluded content

- raw prompts or responses containing personal material;
- secrets, tokens, passphrases, private keys and authentication paths;
- irrelevant account details;
- internal reasoning or unnecessary verbatim text;
- timestamps in the public conversation history.

Public Markdown may retain a protocol date or duration, but not the author's
working time. Redacted information is omitted or marked unpublished, never
replaced with a fabricated time.

## Entry shape

```markdown
## Exchange 000

**Request summary** — …

**Response summary** — …

**Useful trace** — actors, decisions, files and checks.
```

Run metadata may retain dates and durations when required by the protocol.

## Minutes for each run

Every published run has a `PV.md` separate from the general history. It names
the sponsor, experimental orchestrator, candidate agent, consultants and
verifier, then numbers observable mandates, advice, responses, decisions,
corrections and verdicts.

The minutes are evidence-based summaries, not full transcripts. They link
decisions to available files, tests and metrics, identify uncaptured output
and exclude raw internal reasoning. From V2 onwards, each consultant
recommendation records its role and the orchestrator's reasoned disposition:
accepted, rejected or unverifiable.

After every repository-changing exchange, its entry is added before commit.
The commit body records objective, changes and checks, then is pushed unless
the user explicitly says otherwise.
