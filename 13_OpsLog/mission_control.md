# NOESIS / ENERQIS — Mission Control
_Last updated: 2025-09-17 18:55_

## NOW (P0 – do first)
- **Clean working tree** (commit or stash) and re-run `ops_debt_audit.ps1` until **green**.
- **Git identity & SSH hardened** (noreply email, SSH key, verified commits ON).
- **Commit governance pack**: EREP overlays (`ingest_fullcov`, `roadmap_sync`, `ioss`, `prune_sidecars`), hooks (`erep_hooks.yaml`), and **G-OPS-DEBT-ZERO** audit script.
- **Branch protection + CODEOWNERS** on `main` (PR required, status checks, signed commits, no force-push).
- **Secrets**: add `sops/age`, `.sops.yaml`, encrypt `.env.enc`, enable pre-commit secret scan.
- **Risk rails (runtime)**: kill-switch, daily loss cap, position caps — wired into every cBot wrapper.
- **Config signing**: `minisign` strategy configs; runtime verify before enable.

## THIS WEEK (P1)
- **EREP DISCOVERY** (read-only) → Innovation Dossier + backlog refresh.
- **EREP SYNTHESIS PREVIEW** → mechanical fixes auto; editorial changes emitted as **patchsets**.
- **Backtest harness** finalized; add **strategy smoke gate** in CI (toy data).
- **Telemetry & mark-out** wired to NOESIS (slippage, fill quality, 1/5/15m mark-out).

## SOON (Stage‑1 lift)
- Sprint on **Energy‑1**, **Energy‑2**, **CVD‑MR‑1**, **Trend‑TF‑1**.
- Pilot sleeve live (micro) + paper mirror; enable alerts: `loss_cap_trip`, `slippage_3σ`, `gate_fail`.
- Funded evals once pilot metrics stable; then deploy core sleeve.

## BLOCKERS
- Any **red** gate (EREP/IOSS) or **ops debt** > 0.
- Missing `mission_control.md`, backlog, or living scorecard.

## COMMANDS (quick)
```powershell
# Clean tree (commit or stash)
git status
git add -A; git commit -m "ops: clean working tree"  # or: git stash push -m "WIP"

# Re-run ops-debt audit
powershell -ExecutionPolicy Bypass -File .\scripts\ops_debt_audit.ps1
$LASTEXITCODE

# Discovery & Synthesis (preview)
# (Once policy overlays are committed)
# Post in chat: RUN: EREP DISCOVERY
# Post in chat: RUN: EREP SYNTHESIS PREVIEW
```