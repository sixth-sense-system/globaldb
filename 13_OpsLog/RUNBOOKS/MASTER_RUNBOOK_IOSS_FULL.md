# ENERQIS / NOESIS — MASTER RUNBOOK (IOSS FULL)  
_Generated: 2025-09-17 18:55_

This runbook consolidates and de-duplicates all operational instructions (Windows 11 + PowerShell) and orders them **by execution dependency**. It includes sub-steps, why each matters, and exact commands.

---

## 0) Preconditions (verify)
- Windows 11, **Windows Terminal / PowerShell**.
- Installed: **Git for Windows**, **VS Code**, **Python 3.x**.
- GitHub account created.

---

## 1) Git identity + SSH (privacy-first, verified)
**Why:** every commit is immutable; set noreply email; enable SSH + optional commit signing.  
**Do:**
```powershell
# Replace with your GitHub noreply
git config --global user.name  "ENERQIS"
git config --global user.email "<id+username>@users.noreply.github.com"
git config --global user.useConfigOnly true

# SSH
Get-Service ssh-agent | Set-Service -StartupType Automatic
Start-Service ssh-agent
ssh-keygen -t ed25519 -C "<id+username>@users.noreply.github.com"
ssh-add $env:USERPROFILE\.ssh\id_ed25519
ssh -T git@github.com   # expect greeting
```
**Optional (recommended): verified commits via SSH-signing**
```powershell
git config --global gpg.format ssh
git config --global user.signingkey "$env:USERPROFILE\.ssh\id_ed25519.pub"
git config --global commit.gpgsign true
```

---

## 2) VS Code + workspace (quality-of-life)
**Why:** consistent environment, path-aware tasks.  
**Do:** File → Save Workspace As… → `ENERQIS.code-workspace`. Add terminal default: PowerShell; enable Git, Prettier, EditorConfig.

---

## 3) Repo hygiene (line endings, pre-commit)
```powershell
# .gitattributes (normalize)
@'
* text=auto eol=lf
*.ps1  text eol=crlf
*.bat  text eol=crlf
*.cmd  text eol=crlf
*.sh   text eol=lf
*.json  text eol=lf
*.jsonl text eol=lf
*.yaml  text eol=lf
*.yml   text eol=lf
*.md    text eol=lf
*.zip     binary
*.parquet binary
*.png     binary
*.jpg     binary
'@ | Set-Content -Encoding UTF8 .gitattributes

# Pre-commit
pip install pre-commit
pre-commit install
```

---

## 4) Governance pack (EREP overlays + gates + hooks)
**Why:** makes Discovery/Synthesis governed & reproducible; blocks placeholder content; enforces planning freshness.  
**Do:** Ensure these exist and commit:
- `00_repo/.cbr/erep_policy.overlay.ingest_fullcov.json`
- `00_repo/.cbr/erep_policy.overlay.roadmap_sync.json`
- `00_repo/.cbr/erep_policy.overlay.ioss.json`
- `00_repo/.cbr/erep_policy.overlay.prune_sidecars.json`
- `00_repo/.cbr/erep_hooks.yaml` → runs `scripts/ops_debt_audit.ps1` before packaging.
- Acceptance gates include **G-OPS-DEBT-ZERO**, **G-NOPLACEHOLDER**, **G-IIS-***.

```powershell
git add 00_repo\.cbr\erep_policy.overlay.* 00_repo\.cbr\erep_hooks.yaml scripts\ops_debt_audit.ps1
git commit -m "ops(governance): overlays+hooks+gates; enable Discovery/Synthesis under EREP"
git push
```

---

## 5) Branch protection + CODEOWNERS
Enable on GitHub: require PRs, status checks, signed commits, no force-push. Add `CODEOWNERS` for `10_Strategy/`, `risk/`, `tooling/`.

---

## 6) Secrets: sops/age + scans
Add `.sops.yaml`, generate age key, encrypt `.env.enc`, add pre-commit secret scan. Keep real secrets **out** of the repo.

---

## 7) Risk rails (runtime)
Implement shared module (kill-switch, daily loss cap, position caps) and wire to each cBot. Add **config signing** via `minisign` and **runtime verify**.

---

## 8) IOSS run — CONSOLIDATE (this output)
- Consolidated all instruction dumps into this **MASTER RUNBOOK** and a **Steps Checklist CSV** (below).

---

## 9) Discovery & Synthesis (governed)
- **RUN: EREP DISCOVERY** → Innovation Dossier + backlog refresh.
- **RUN: EREP SYNTHESIS PREVIEW** → mechanical auto-fix; editorial **patchsets** only → PR.

---

## 10) CI/Quality gates
Add build/style/test gates for strategy code; minimal “smoke backtest” gate (toy data) in CI.

---

## 11) Data ingestion (ERIP/IIS)
- Books/repos/papers (PIT-correct, leakage-safe).
- Emit **Skill Capsules** and update **Theory**/**Profiles** via Synthesis (patchsets).

---

## 12) Strategy Factory
- Sprint on Energy‑1/2, CVD‑MR‑1, Trend‑TF‑1.
- Backtest harness final; acceptance dashboards; promotion criteria.

---

## 13) Ops: snapshot, verify, sign, offsite
- Package under EREP FULL; verify manifest; PGP-sign; offsite copy (S3 Glacier IR).

---

### Sanity commands
```powershell
git status
powershell -ExecutionPolicy Bypass -File .\scripts\ops_debt_audit.ps1
$LASTEXITCODE
```