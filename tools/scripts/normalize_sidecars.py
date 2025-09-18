#!/usr/bin/env python3
# Normalize sidecar metadata:
# - Ensure each JSON file has an `.erqmeta.json` sidecar (preferred).
# - If a legacy `<file>.meta.json` exists but `.erqmeta.json` does not, copy/rename it.
# - If both exist, keep `.erqmeta.json` and (optionally) delete the legacy file with `--delete-legacy`.
import argparse, json, sys
from pathlib import Path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".", help="Repo root")
    ap.add_argument(
        "--delete-legacy",
        action="store_true",
        help="Delete *.meta.json when *.erqmeta.json is present",
    )
    args = ap.parse_args()

    root = Path(args.root).resolve()
    moved = deleted = created = 0
    for p in root.rglob("*.json"):
        if p.name.endswith(".meta.json") or p.name.endswith(".erqmeta.json"):
            continue
        legacy = p.with_suffix(p.suffix + ".meta.json")
        prefer = p.with_suffix(p.suffix + ".erqmeta.json")
        if prefer.exists():
            if legacy.exists() and args.delete_legacy:
                try:
                    legacy.unlink()
                    deleted += 1
                except Exception as e:
                    print(f"ERROR deleting {legacy}: {e}", file=sys.stderr)
            continue
        if legacy.exists():
            try:
                prefer.write_text(legacy.read_text(encoding="utf-8"), encoding="utf-8")
                moved += 1
                if args.delete_legacy:
                    legacy.unlink()
                    deleted += 1
            except Exception as e:
                print(f"ERROR migrating {legacy} -> {prefer}: {e}", file=sys.stderr)
        else:
            # create minimal sidecar scaffold
            try:
                prefer.write_text(
                    json.dumps({"_note": "add ERQ-META here if required"}, indent=2),
                    encoding="utf-8",
                )
                created += 1
            except Exception as e:
                print(f"ERROR creating {prefer}: {e}", file=sys.stderr)

    print(
        json.dumps(
            {"migrated": moved, "deleted_legacy": deleted, "created_scaffold": created}
        )
    )


if __name__ == "__main__":
    main()
