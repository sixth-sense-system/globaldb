# ISS: CONSOLIDATION + PREVIEW — Preflight Checklist
generated: 2025-09-24T21:33:04Z

## Repo hygiene
- [ ] create feature branch (e.g., opslog/all-time-baseline)
- [ ] ensure no working tree changes; run pre-commit locally

## Governance & CI
- [ ] verify 00_repo/.cbr/erep_policy.json is authoritative; remove overlays file if present
- [ ] required checks set: erep, erep-guard, erep-equivalence, pre-commit, codeql, opslog-sync
- [ ] workflows pinned by SHA (see tooling README below)

## Overlay scope
- [ ] include_globs in 13_OpsLog/overlays/semantic_preview/config/semantic_overlay.yaml cover repo + transcripts
- [ ] (optional) add 11_Research/ and 10_AI_Algo/ notes, then rerun overlay

## Run sequence
- [ ] run semantic overlay to produce evidence_tickets.jsonl
- [ ] review tickets ≥ 0.72 confidence; promote to SSOT (events/roadmap/decisions/configs)
- [ ] trigger opslog-sync → download opslog-ci → verify 6 views + mission control
- [ ] PR with artifacts; EREP gates green; merge to main

## Post-merge
- [ ] schedule TRUE SYNTHESIS pass (Discovery/Synthesis overlays)
- [ ] add sops/age & config signing if not yet in place
