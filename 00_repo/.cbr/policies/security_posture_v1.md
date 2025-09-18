# Security Posture — Stage‑1 Baseline (v1.0)
**Updated:** 2025-09-16 16:09

## Objectives
Protect code/IP, secrets, and operations while enabling fast iteration.

## Controls (Stage‑1)
1. **Identity & Access**
   - Git `user.name` and **GitHub noreply** `user.email` configured.
   - 2FA required on GitHub; SSH keys (ed25519) with passphrase.
2. **Repo Hygiene**
   - Branch protection on `main`: PRs only, required checks, no force-push.
   - `.gitattributes` normalization; `.gitignore` excludes; `.env.template` present.
3. **Secrets Management**
   - `sops` + `age` enforced via `.sops.yaml`; secrets committed only as `*.enc`.
   - Pre-commit secret scanners enabled.
4. **CI/CD Supply Chain**
   - GitHub Actions **pinned by SHA**; CodeQL enabled; Dependabot (security + versions).
5. **Dependency hygiene**
   - SBOM (CycloneDX) on snapshots; license headers for source files.
6. **Runtime Safeguards**
   - Shared risk rails (kill-switch, daily loss cap, position caps).
   - **Config signing** (minisign) + runtime verify.
7. **Data & Provenance**
   - Snapshots with SHA‑256 manifest; dataset manifests; frozen evaluation splits.
8. **Backups & Recovery**
   - Daily encrypted offsite snapshot; quarterly restore test.
9. **LLM Usage Policy**
   - No proprietary code to public endpoints; redact; local-only for sensitive contexts.
10. **Monitoring & Incidents**
   - NOESIS alerts: loss_cap_trip, slippage_3σ, gate_fail.
   - Incident runbooks and templates checked in.

## Verification
Each control maps to EREP gates under `SECURITY:baseline:v1` and/or manual checks documented in Ops entries.
