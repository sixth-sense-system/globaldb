#!/usr/bin/env python3
"""
Fail CI if any GitHub Actions uses entries are unpinned (e.g., @v4).
Allowed: 40-hex SHAs, local actions (./path).
"""
import re, sys, glob


def main():
    bad = []
    for wf in glob.glob(".github/workflows/*.y*ml"):
        txt = open(wf, "r", encoding="utf-8").read()
        for m in re.finditer(r"uses:\s*([^\s]+)", txt):
            ref = m.group(1).strip()
            if ref.startswith("./"):
                continue
            if "@" not in ref:
                bad.append((wf, ref, "missing @ref"))
                continue
            ver = ref.split("@", 1)[1]
            if not re.fullmatch(r"[0-9a-fA-F]{40}", ver):
                bad.append((wf, ref, "not pinned to 40-hex SHA"))
    if bad:
        print("Unpinned GitHub Actions detected:")
        for wf, ref, why in bad:
            print(f" - {wf}: {ref} ({why})")
        sys.exit(1)
    print("All GitHub Actions are pinned to SHAs.")


if __name__ == "__main__":
    main()
