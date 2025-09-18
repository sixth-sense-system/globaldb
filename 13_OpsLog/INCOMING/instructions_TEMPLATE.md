# Instructions Dump — Template

Write freely (paragraphs ok). Headings like `### STEP:` help.
Code blocks will be captured to the Tech Ops cheatsheet.

### STEP: Install Git (Windows)
- Download official Git for Windows from https://gitforwindows.org/
- Choose PATH: "Use Git from the command line..."
- Verify:
```powershell
git --version
```

### STEP: Configure Git identity (noreply)
- GitHub Settings → Emails → copy noreply
```powershell
git config --global user.name "ENERQIS"
git config --global user.email "<id>+<user>@users.noreply.github.com"
git config --global --get user.email
```

### STEP: Enable EREP overlays & gates
```powershell
git add 00_repo\.cbr\erep_policy.overlay.*.json 00_repo\.cbr\acceptance_gates*.yaml 00_repo\.cbr\erep_hooks.yaml
git commit -m "chore(erep): update overlays/gates/hooks"
```

### STEP: Run EREP DISCOVERY
- Post here: RUN: EREP DISCOVERY
- Expect: innovation dossier + backlog updates

### STEP: Drain INBOX after ingest
```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\inbox_after_ingest.ps1
```

### STEP: Full package (dry-run first)
```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\ops_debt_audit.ps1
```
