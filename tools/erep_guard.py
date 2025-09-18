#!/usr/bin/env python3
import argparse, os, sys, json, re, pathlib

TEXT_EXTS = ('.md','.markdown','.txt','.yaml','.yml','.rst','.py')
BLOCK_ERRORS = 0

def is_text(path):
    return path.suffix.lower() in TEXT_EXTS

def read_text_safe(path, limit=2_000_000):
    try:
        with open(path, 'rb') as f:
            return f.read(limit).decode('utf-8','ignore')
    except Exception:
        return ''

def try_json(text):
    try:
        import json
        return json.loads(text)
    except Exception:
        return None

def strip_chain(p: str) -> str:
    while p.endswith('.meta.json') or p.endswith('.erqmeta.json'):
        if p.endswith('.meta.json'):
            p = p[:-len('.meta.json')]
        else:
            p = p[:-len('.erqmeta.json')]
    return p

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--repo', required=True)
    ap.add_argument('--max-path-length', type=int, default=180)
    args = ap.parse_args()

    repo = pathlib.Path(args.repo).resolve()
    errors = []
    warnings = []

    # Disallow patterns
    for p in repo.rglob('*'):
        rel = p.relative_to(repo).as_posix()
        if p.is_dir():
            continue
        lrel = rel.lower()

        # Exclude standard noise
        if '/.git/' in f'/{lrel}/' or lrel.endswith('.ds_store') or '/__pycache__/' in f'/{lrel}/':
            continue

        # 1) No nested zips in repo
        if lrel.endswith('.zip'):
            errors.append((rel, 'NESTED_ZIP_FORBIDDEN'))

        # 2) No .erqmeta.json anywhere
        if lrel.endswith('.erqmeta.json') or '.erqmeta.json.' in lrel:
            errors.append((rel, 'ERQ_SIDECAR_FORBIDDEN'))

        # 3) No chainy sidecars (more than one suffix)
        def count_segments(s):
            c=0; t=s
            while t.endswith('.meta.json') or t.endswith('.erqmeta.json'):
                if t.endswith('.meta.json'):
                    t = t[:-len('.meta.json')]
                else:
                    t = t[:-len('.erqmeta.json')]
                c+=1
            return c
        if lrel.endswith('.meta.json') or lrel.endswith('.erqmeta.json') or '.meta.json.' in lrel or '.erqmeta.json.' in lrel:
            if count_segments(lrel) > 1:
                errors.append((rel, 'SIDECAR_CHAIN_FORBIDDEN'))

        # 4) Path length limit
        if len(rel) > args.max_path_length:
            errors.append((rel, f'PATH_LENGTH>{args.max_path_length}'))

    # 5) Redundant sidecars on embedded parents; JSON array must have exactly one sidecar
    # Build sidecar map
    sidecars = {}
    for p in repo.rglob('*'):
        rel = p.relative_to(repo).as_posix()
        if p.is_file():
            lrel = rel.lower()
            if lrel.endswith('.meta.json') or lrel.endswith('.erqmeta.json') or '.meta.json.' in lrel or '.erqmeta.json.' in lrel:
                parent = strip_chain(rel)
                sidecars.setdefault(parent, []).append(rel)

    for parent, scs in sidecars.items():
        parent_path = repo / parent
        if not parent_path.exists():
            errors.append((parent, 'SIDECAR_ORPHAN'))
            continue
        suf = parent_path.suffix.lower()
        if suf in TEXT_EXTS:
            if 'ERQ-META-BEGIN' in read_text_safe(parent_path):
                errors.append((parent, 'REDUNDANT_SIDECAR_ON_EMBEDDED_PARENT'))
        elif suf == '.json':
            js = try_json(read_text_safe(parent_path))
            if isinstance(js, dict) and '_erq_meta' in js:
                errors.append((parent, 'REDUNDANT_SIDECAR_ON_EMBEDDED_PARENT'))
            if isinstance(js, list):
                if len(scs) == 0:
                    errors.append((parent, 'JSON_ARRAY_MISSING_SIDECAR'))
                elif len(scs) > 1:
                    errors.append((parent, 'JSON_ARRAY_MULTIPLE_SIDECARS'))
        # Uniqueness
        if len(scs) > 1:
            errors.append((parent, 'MORE_THAN_ONE_SIDECAR'))

    if errors:
        print('EREP GUARD: FAIL')
        for rel, issue in errors:
            print(f'::error file={rel}::{issue}')
        sys.exit(1)

    print('EREP GUARD: PASS')
    sys.exit(0)

if __name__ == '__main__':
    main()
