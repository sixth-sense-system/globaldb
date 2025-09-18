mkdir -Force "13_OpsLog" | Out-Null

@"
# Mission Control — ENERQIS
Date: $(Get-Date -Format "yyyy-MM-dd HH:mm K")

## Today’s Focus
- Keep the pipeline green (COMPLIANCE → FULL PACKAGE under gates).
- Prepare backlog & living scorecard for Strategy Factory kickoff.

## This Week (P0)
- Finish governance wiring (hooks/gates/overlays audited).
- Backlog ingestion & dedupe passes; promote P0 tasks into scorecard.

## Gate Posture (snapshot)
- Ops debt audit: will be green after this file is saved.
- Backlog CSV present; Living Scorecard CSV present.

## Next Actions (you can edit freely)
1. Run ops_debt_audit.ps1 and confirm exit 0.
2. OPEN: ERIP/IIS passes for idea capture and roadmap sync.
3. If green, run EREP FULL PACKAGE and post Ops entry.

## Notes
Mission Control is the daily cockpit: it should be updated on each packaging cycle and whenever priorities change. This keeps planning surfaces in sync with gates and ensures deterministic, auditable releases.
"@ | Set-Content -Encoding utf8 "13_OpsLog\mission_control.md"
