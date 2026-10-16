#!/usr/bin/env python3
"""Audit repository Markdown links offline, including references and HTML assets.

Checks tracked Markdown and newly added editorial Markdown. Remote HTTP health
and VS Code's rendering are not tested. GitHub heading anchors are approximated;
unsupported Markdown constructs must be reviewed rather than silently rewritten.
"""

from html import unescape
from pathlib import Path
import re
import subprocess
import unicodedata
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
# Visible candidate messages are historical evidence: do not rewrite them.
# Replacement navigation is published in docs/parallel-pilot.md and translations.
HISTORICAL_TARGETS = {
    ('runs/astra-medium-core-v2-2-supervised-002/PV.md', '<private-run-root>/workspace/solution/calculator.py'),
    ('runs/astra-medium-core-v2-2-supervised-002/PV.md', '<private-run-root>/workspace/solution/README.md'),
    ('runs/astra-medium-scientific-v2-2-lean-002/PV.md', 'scientific_calculator.py'),
    ('runs/astra-medium-scientific-v2-2-lean-002/PV.md', 'README.md'),
}


def prose(text):
    """Remove fenced code so examples are not treated as live navigation."""
    return re.sub(r"^(`{3,}|~{3,})[^\n]*\n.*?^\1\s*$", "", text,
                  flags=re.M | re.S)


def targets(text):
    text = prose(text)
    definitions = dict(re.findall(r"^\s{0,3}\[([^]\n]+)\]:\s*<?([^\s>]+)>?", text, re.M))
    definitions = {key.casefold(): value for key, value in definitions.items()}
    found = re.findall(r"\]\(\s*(<[^>]+>|[^\s)]+)(?:\s+\"[^\"]*\")?\s*\)", text)
    for label, reference in re.findall(r"\[([^]\n]+)\]\[([^]\n]*)\]", text):
        key = (reference or label).casefold()
        if key in definitions:
            found.append(definitions[key])
    found.extend(definitions.values())
    found.extend(re.findall(r'\b(?:src|href)=["\']([^"\']+)["\']', text))
    for srcset in re.findall(r'\bsrcset=["\']([^"\']+)["\']', text):
        found.extend(part.strip().split()[0] for part in srcset.split(',') if part.strip())
    return [unescape(target[1:-1] if target.startswith('<') and target.endswith('>') else target) for target in found]


def anchors(text):
    result = set(re.findall(r'\b(?:id|name)=["\']([^"\']+)["\']', text))
    seen = {}
    for heading in re.findall(r'^ {0,3}#{1,6}\s+(.+?)\s*#*$', prose(text), re.M):
        heading = re.sub(r'\[([^]]+)\]\([^)]*\)', r'\1', heading)
        heading = unescape(re.sub(r'<[^>]+>', '', heading)).lower()
        slug = ''.join(c for c in heading if c in '-_ ' or unicodedata.category(c)[0] in 'LN').replace(' ', '-')
        count = seen.get(slug, 0)
        seen[slug] = count + 1
        result.add(slug + (f'-{count}' if count else ''))
    return result


def inspect(paths, root=ROOT, historical=None):
    errors, remote = [], set()
    count = 0
    for path in paths:
        for target in targets(path.read_text(encoding='utf-8')):
            count += 1
            if 'vscode-resource' in target or 'vscode-cdn.net' in target or target.startswith('vscode-remote:'):
                errors.append(f'{path.relative_to(root)}: non-portable editor URL: {target}')
                continue
            url = urlsplit(target)
            if url.scheme or url.netloc:
                remote.add(target)
                continue
            destination = path.parent / unquote(url.path) if url.path else path
            if not destination.exists():
                key = (str(path.relative_to(root)), target)
                if historical is not None and key in HISTORICAL_TARGETS:
                    historical.append(f'{key[0]}: preserved historical target: {target}')
                else:
                    errors.append(f'{path.relative_to(root)}: missing target: {target}')
            elif url.fragment and destination.suffix.lower() == '.md':
                if unquote(url.fragment) not in anchors(destination.read_text(encoding='utf-8')):
                    errors.append(f'{path.relative_to(root)}: anchor to review: {target}')
    return count, remote, errors


def main():
    names = subprocess.check_output(['git', 'ls-files', '-z', '--', '*.md', '*.MD'], cwd=ROOT).decode().split('\0')
    paths = {ROOT / name for name in names if name}
    for folder in ('docs', 'results'):
        paths.update((ROOT / folder).rglob('*.md'))
    historical = []
    count, remote, errors = inspect(sorted(paths), historical=historical)
    print(f'Markdown files: {len(paths)}; links/assets: {count}; external URLs (not fetched): {len(remote)}')
    for warning in historical:
        print(warning)
    print(f'Historical unavailable links: {len(historical)}; new errors: {len(errors)}')
    for error in errors:
        print(error)
    return bool(errors)


if __name__ == '__main__':
    raise SystemExit(main())
