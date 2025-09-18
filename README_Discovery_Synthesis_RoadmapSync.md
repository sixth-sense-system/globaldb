# Discovery/Synthesis + Roadmap Sync Kit — v1.3
Generated: 2025-09-16 01:36

**Process:** Discovery/Synthesis Run (IIS → Synthesis → Roadmap Sync)

## Run (PowerShell)
```powershell
.\scripts\iis_ingest.ps1 -Input ".\INBOX\ideas" -Mode txtmd
.\scripts\synthesis_run.ps1 -ExtractDir "._OpsLog\DERIVED\extract\latest" `
  -BacklogCsv ".\enerqis_backlog.csv" -BacklogMd ".\enerqis_backlog.md"
.\scriptsoadmap_sync.ps1 -BacklogCsv ".\enerqis_backlog.csv" -BacklogMd ".\enerqis_backlog.md"
```
