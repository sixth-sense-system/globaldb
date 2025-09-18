# RUN: RUNBOOK CONSOLIDATE (IOSS) — v1.1

**Scope:** Consolidate instructions into MASTER_RUNBOOK + steps CSV + progress tracker + tech-ops cheatsheet
**Outcome:** Deduped, ordered, *updated* instructions with required overlays/gates/hooks and commit/dry-run blocks injected.

## Checklist
1. Place input file: `13_OpsLog/INCOMING/instructions_<DATE>.md`
2. Run: `powershell -ExecutionPolicy Bypass -File .\scripts\ioss_compile.ps1 -Input "13_OpsLog\INCOMING\instructions_<DATE>.md"`
3. Review outputs and commit on `ops/runbook-<DATE>` branch.
