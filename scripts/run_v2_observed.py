#!/usr/bin/env python3
"""Future runs only: call the frozen V2 runner with a content-free observer.

Use the same --run / --challenge arguments as run_v2.py. This is opt-in:
record this wrapper and observe_sessions.py hashes in future run metadata.
The original runner, prompts, sessions and candidate permissions are unchanged.
"""

import run_v2
from observe_sessions import SessionObserver, v2_topology


def main():
    observer = SessionObserver()
    topology = v2_topology()
    original = run_v2.run_session

    def observed(**kwargs):
        return observer.invoke(original, topology[kwargs["label"]], **kwargs)

    run_v2.run_session = observed
    try:
        return run_v2.main()
    finally:
        run_v2.run_session = original


if __name__ == "__main__":
    raise SystemExit(main())
