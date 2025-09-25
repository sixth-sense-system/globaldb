# ISS: CONSOLIDATION + PREVIEW — All‑Time Baseline

> **Purpose**: Govern a deterministic, repeatable consolidation and preview of the org state, using HSESF (Human‑in‑the‑loop, Safety, Ethics, Security, and Fidelity) principles. Outputs are preview artefacts; the System of Record (SSOT) remains append‑only and is never mutated by this workflow.

## Profiles
- **CONS**: Consolidate inputs → SSOT (append‑only). (Preview only in this scaffold)
- **DISC**: Discovery digest from recent ops logs and threads.
- **SYNTH**: Synthesis & deltas vs. last baseline.
- **OPSLOG_SYNC**: Generate consumable views (Scorecard, Mission Control, etc.).

## Inputs → SSOT → Views
- **Inputs** (read‑only): `13_OpsLog/inputs/**`, `13_OpsLog/events/**`, repo metadata, PRs.
- **SSOT** (append‑only): `13_OpsLog/ssot/**` (not mutated by this scaffold; wire a renderer later).
- **Views** (overwrite allowed): `13_OpsLog/views/**`, `05_Blueprint/MASTER/mission_control.md`.

## HSESF Controls
- **Determinism**: Fixed seeds; pinned Actions; no network calls in render step.
- **Safety & Security**: No secrets used; SOPS enforced in preflight; preview not committing to main.
- **Ethics & Fidelity**: Provenance headers; explicit limitations; human review required.

## Outputs (Preview Artefacts)
- `13_OpsLog/views/scorecard.md` — Scorecard v2
- `13_OpsLog/views/blueprint_delta.md` — What changed in plans
- `13_OpsLog/views/mission_control.md` — Live mission control snapshot (also mirrored to `05_Blueprint/MASTER/mission_control.md`)
- `13_OpsLog/views/opslog_digest.md` — Operational digest (last window)
- `13_OpsLog/views/repo_delta.md` — Repo changes since prior baseline
- `13_OpsLog/views/risk_register.md` — Risks/mitigations (preview)

> In this scaffold the renderer generates placeholders so CI passes; replace `tools/opslog-render.ps1` with your real SSOT pipeline when ready.

## Scorecard v2 (Structure)
- **Headline Scores** (0–10) with **Levers to 9.5–10** for each dimension.
- **Why scores moved** (since last baseline), **Top 5 wins**, **Top 5 risks**.
- **Probability‑weighted outcomes** and **valuation impact**.
- **Message to Our People** (plain‑speak narrative).

## Runbook
1. **Preflight** (local or CI): `.\tools\iss-preflight.ps1`
2. **Render** (CI): `tools/opslog-render.ps1` → writes preview views.
3. **Review artefact**: GitHub Actions artifact `opslog-views`.
4. **(Optional) Commit promotion**: open a PR that replaces placeholders with the curated output.

## Governance
- No direct commits to main from ISS jobs.
- All Actions **pinned to SHAs**.
- SOPS/age baseline must be healthy or job fails.
- Overlay edits permitted only in preview views folders.
