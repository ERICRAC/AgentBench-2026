#!/usr/bin/env python3
"""Offline parallel transport rehearsal: disposable fake candidates, no models.

Reuse the existing process sandbox without changing any frozen runner.
This verifies local subprocess isolation, not an authenticated model transport.
"""

import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile
import time

from v2_2_transport import isolated_command

ROOT = Path(__file__).resolve().parents[1]
OWNERS = {'DEV-A': {'engine.py'}, 'DEV-B': {'presentation.py', 'cli.py', 'README.md'}}


def snapshot(directory, expected):
    """Fail closed on missing/extra files or symlinks before integration."""
    entries = list(directory.iterdir())
    if {p.name for p in entries} != set(expected):
        raise ValueError('Missing or out-of-scope deliverable')
    if any(p.is_symlink() or not p.is_file() for p in entries):
        raise ValueError('Non-regular deliverable')
    return {p.name: p.read_bytes() for p in entries}


def hashes(files):
    return {name: hashlib.sha256(value).hexdigest() for name, value in sorted(files.items())}


def check():
    records, processes = [], []
    with tempfile.TemporaryDirectory(prefix='.parallel-fixture-', dir=ROOT) as folder:
        root = Path(folder)
        epoch = time.monotonic()
        try:
            for role in OWNERS:
                workspace = root/role
                (workspace/'solution').mkdir(parents=True)
                (workspace/'CHALLENGE.md').write_text('SIMULATION ONLY')
                (workspace/'canary.txt').write_text('private synthetic peer data')
            for role, expected in OWNERS.items():
                workspace = root/role
                peer = root/('DEV-B' if role == 'DEV-A' else 'DEV-A')/'canary.txt'
                (workspace/'solution'/'escape').symlink_to(peer)
                code = '''import json, pathlib, sys, time
def allowed(action):
    try:
        action()
        return True
    except OSError:
        return False
peer = pathlib.Path(PEER)
checks = {
    'own_contract_read': allowed(lambda: pathlib.Path('../CHALLENGE.md').read_text()),
    'peer_read_denied': not allowed(peer.read_text),
    'peer_write_denied': not allowed(lambda: peer.write_text('changed')),
    'symlink_escape_denied': not allowed(lambda: pathlib.Path('escape').read_text()),
    'symlink_write_denied': not allowed(lambda: pathlib.Path('escape').write_text('changed')),
    'contract_write_denied': not allowed(lambda: pathlib.Path('../CHALLENGE.md').write_text('changed')),
}
pathlib.Path('escape').unlink()
print('READY', flush=True)
assert sys.stdin.readline().strip() == 'GO'
time.sleep(0.1)
for name in FILES:
    pathlib.Path(name).write_text('SIMULATION ONLY: ' + name)
print(json.dumps(checks), flush=True)
'''.replace('PEER', repr(str(peer))).replace('FILES', repr(sorted(expected)))
                command = isolated_command('MAIN', workspace, ['/usr/bin/python3', '-B', '-c', code])
                started = time.monotonic()-epoch
                process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                           stderr=subprocess.PIPE, text=True)
                processes.append((role, process, started))
            # Readiness uses pipe notifications with a bounded watchdog below:
            # readers wait at most 10 s; failures cannot leave the other child alive.
            import selectors
            selector = selectors.DefaultSelector()
            for role, process, started in processes:
                selector.register(process.stdout, selectors.EVENT_READ, role)
            ready = set()
            deadline = time.monotonic()+10
            while len(ready) < len(processes):
                if time.monotonic() >= deadline:
                    raise TimeoutError('Fake candidates did not become ready')
                for key, mask in selector.select(timeout=0.1):
                    if key.fileobj.readline().strip() != 'READY':
                        raise RuntimeError('Isolation unavailable or fake candidate failed before readiness')
                    ready.add(key.data)
                    selector.unregister(key.fileobj)
            selector.close()
            released = time.monotonic()-epoch
            for role, process, started in processes:
                process.stdin.write('GO\n')
                process.stdin.flush()
            # Both are running before either is collected. A process return is
            # recorded on collection, not mislabelled as exact kernel exit time.
            for role, process, started in processes:
                stdout, stderr = process.communicate(timeout=10)
                observed = time.monotonic()-epoch
                if process.returncode:
                    raise RuntimeError(f'{role}: subprocess failed: {stderr[:200]}')
                checks = json.loads(stdout)
                if not all(checks.values()):
                    raise RuntimeError(f'{role}: isolation probe failed')
                files = snapshot(root/role/'solution', OWNERS[role])
                records.append({'role': role, 'started_relative_s': started,
                                'completion_observed_relative_s': observed,
                                'checks': checks, 'sha256': hashes(files), 'usage': None})
            workspace = root/'INT'
            (workspace/'solution').mkdir(parents=True)
            (workspace/'CHALLENGE.md').write_text('SIMULATION ONLY')
            for role in OWNERS:
                for name, content in snapshot(root/role/'solution', OWNERS[role]).items():
                    (workspace/'solution'/name).write_bytes(content)
            expected = set.union(*OWNERS.values())
            before = hashes(snapshot(workspace/'solution', expected))
            integration_start = time.monotonic()-epoch
            code = "from pathlib import Path; p=Path('engine.py'); p.write_text(p.read_text()+'\\nINTEGRATED FIXTURE')"
            result = subprocess.run(isolated_command('MAIN', workspace, ['/usr/bin/python3', '-B', '-c', code]),
                                    capture_output=True, text=True, timeout=10)
            if result.returncode:
                raise RuntimeError('Fake integrator failed')
            after = hashes(snapshot(workspace/'solution', expected))
            changed = [name for name in before if before[name] != after[name]]
            if changed != ['engine.py']:
                raise RuntimeError('Unexpected integration change')
            for role in OWNERS:
                if (root/role/'canary.txt').read_text() != 'private synthetic peer data':
                    raise RuntimeError('Peer canary changed')
            return {'status': 'passed', 'kind': 'local_isolated_process_simulation',
                    'model_calls': 0, 'official_verdict': None, 'usage': None,
                    'protocol_frozen': False, 'live_authorized': False,
                    'sessions': records, 'both_ready_before_release': len(ready) == 2,
                    'release_relative_s': released, 'integration_start_relative_s': integration_start,
                    'integration_after_both_collected': integration_start >= max(r['completion_observed_relative_s'] for r in records),
                    'integration_changed_files': changed, 'assembled_sha256': before, 'final_sha256': after,
                    'wall_seconds': time.monotonic()-epoch,
                    'limitations': ['Fake candidates only; no authenticated model transport',
                                    'Completion timestamps are parent observations, not exact process exit times',
                                    'No token accounting or quota claim; simulation has no calculator score']}
        finally:
            for role, process, started in processes:
                if process.poll() is None:
                    process.kill()
                process.communicate()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--simulate', action='store_true', required=True)
    parser.parse_args()
    try:
        print(json.dumps(check(), indent=2))
    except (OSError, RuntimeError, ValueError, TimeoutError, subprocess.TimeoutExpired) as error:
        print(json.dumps({'status': 'blocked', 'model_calls': 0, 'error': str(error)}))
        raise SystemExit(1)
