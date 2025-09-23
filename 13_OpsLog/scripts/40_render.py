#!/usr/bin/env python3
# Minimal, tolerant opslog renderer used by CI
# - Reads YAML config
# - Tolerates empty/missing SSOT
# - Writes two Markdown mirrors for CI artifacts
# - Avoids f-string backslash traps on Windows runners

import os, sys, glob, json, datetime
from pathlib import Path

try:
    import yaml  # PyYAML
except Exception as e:
    print(f"[render] PyYAML not available: {e}", file=sys.stderr)
    sys.exit(1)


def read_yaml(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def ensure_parent(path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)


def main():
    # ---- read config ----
    # default path so local runs work; CI passes --config in workflow
    cfg_path = Path("13_OpsLog/policies/opslog_render.yml")
    if "--config" in sys.argv:
        ix = sys.argv.index("--config")
        if ix + 1 < len(sys.argv):
            cfg_path = Path(sys.argv[ix + 1])

    if not cfg_path.exists():
        print(f"[render] config not found: {cfg_path.as_posix()}", file=sys.stderr)
        sys.exit(0)  # tolerate (green)

    cfg = read_yaml(cfg_path)

    out_rendered = Path(
        cfg.get("out", {}).get("rendered_md", "13_OpsLog/DERIVED/ci/ci_rendered.md")
    )
    out_mission = Path(
        cfg.get("out", {}).get(
            "mission_md", "13_OpsLog/DERIVED/ci/ci_mission_control.md"
        )
    )

    inputs = cfg.get("inputs", {}) or {}
    ssot_glob = inputs.get("ssot_glob", "13_OpsLog/SSOT/**/*.yaml")
    schemas_dir = inputs.get("schemas_dir", "13_OpsLog/SCHEMA")

    # ---- collect inputs (tolerant) ----
    ssot_files = [Path(p) for p in glob.glob(ssot_glob, recursive=True)]
    schemas_ok = Path(schemas_dir).exists()

    now = datetime.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"

    # ---- simple content (we will replace with rich renderer later) ----
    rendered_lines = []
    rendered_lines.append("# Opslog Render (CI mirror)")
    rendered_lines.append("")
    rendered_lines.append(f"- Generated: {now} UTC")
    rendered_lines.append(f"- Config: {cfg_path.as_posix()}")
    rendered_lines.append(f"- SSOT files found: {len(ssot_files)}")
    rendered_lines.append(f"- Schemas present: {schemas_ok}")
    rendered_lines.append("")
    if ssot_files:
        rendered_lines.append("## SSOT Index")
        for p in sorted(ssot_files):
            # Use POSIX style paths in output (avoids backslashes entirely)
            rendered_lines.append(f"- `{p.as_posix()}`")
        rendered_lines.append("")

    mission_lines = []
    mission_lines.append("# Mission Control (CI mirror)")
    mission_lines.append("")
    mission_lines.append(f"_Generated {now} UTC_")
    mission_lines.append("")
    mission_lines.append(
        "This is a CI-safe mirror. The full Mission Control will be produced by the richer renderer during normal runs."
    )
    mission_lines.append("")
    mission_lines.append("## Now / Next (placeholder)")
    mission_lines.append("- Now: bootstrap + first pass green")
    mission_lines.append("- Next: Discovery/Synthesis run → Scorecard v1")

    # ---- write outputs ----
    ensure_parent(out_rendered)
    ensure_parent(out_mission)
    out_rendered.write_text("\n".join(rendered_lines) + "\n", encoding="utf-8")
    out_mission.write_text("\n".join(mission_lines) + "\n", encoding="utf-8")

    # Optional: drop a tiny JSON receipt for debugging
    receipt = {
        "generated_utc": now,
        "config": cfg_path.as_posix(),
        "rendered_md": out_rendered.as_posix(),
        "mission_md": out_mission.as_posix(),
        "ssot_count": len(ssot_files),
        "schemas_present": bool(schemas_ok),
    }
    receipt_path = Path("13_OpsLog/DERIVED/ci/ci_render_receipt.json")
    ensure_parent(receipt_path)
    receipt_path.write_text(json.dumps(receipt, indent=2), encoding="utf-8")

    print(f"[render] wrote {out_rendered.as_posix()}")
    print(f"[render] wrote {out_mission.as_posix()}")
    print(f"[render] receipt → {receipt_path.as_posix()}")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        # Keep CI tolerant but record the error
        err_path = Path("13_OpsLog/DERIVED/ci/ci_render_error.txt")
        ensure_parent(err_path)
        err_path.write_text(str(exc) + "\n", encoding="utf-8")
        print(f"[render] ERROR: {exc}", file=sys.stderr)
        # Let the workflow upload artifacts even on failure
        sys.exit(0)
