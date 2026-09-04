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
After every repository-changing exchange, its entry is added before commit.
The commit body records objective, changes and checks, then is pushed unless
the user explicitly says otherwise.
