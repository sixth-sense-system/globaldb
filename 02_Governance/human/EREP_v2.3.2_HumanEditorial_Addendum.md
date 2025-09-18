# ERQ-META-BEGIN
# {"doc_type": "policy", "spec_version": "2.3.2", "source_baseline_hash": "sha256:f45730d0e5e6110637c235796291081468f18179306ff4f723790b7a57138754", "provenance": {"build_id": "61fa8c82-47e5-4962-bd41-bb4cb1d22568", "builder": "EREP v2.3.2 policy-generator", "built_at": "2025-09-12T07:29:21Z", "tools": {"python": "3.11.8", "hash": "sha256"}}, "governance_links": {"acceptance_gates": "00_repo/.cbr/acceptance_gates.yaml", "registry": "00_repo/.cbr/registry.json", "audit_log": "00_repo/.cbr/audit_log.json"}, "canonicalization": {"encoding": "utf-8", "newline": "LF", "sort_keys": true}, "integrity": {"algo": "sha256", "canonical_scope": "payload", "value": "f45730d0e5e6110637c235796291081468f18179306ff4f723790b7a57138754"}}
# ERQ-META-END
# ENERQIS — EREP v2.3.2 Editorial Enrichment & Quality Gates (Read-Only)

**Purpose:** Formalizes human-content enrichment under governance. Editorial edits default to **PROPOSE**; AUTO_MINOR is capped (≤200 chars or ≤2%). All artifacts remain ERQ-META, deterministic, auditable.

---

## Modes
- PROPOSE (default) · AUTO_MINOR · OFF

## Safeguards
- Protected sections: ['Executive summary', 'Risks', 'Governance', 'Escalation']
- Minor caps: {'max_chars': 200, 'max_percent': 2.0}
- Major caps: {'max_files_per_run': 10, 'min_rationale_words': 25}; freeze 7 days after major.
- Sources required for factual changes; allowed roots: ['00_repo/.cbr/reports/**', '03_Data/**', '11_Research/**'].

## Outputs
- Editorial summary: `00_repo/.cbr/reports/editorial_changes.md` (+ JSON)
- Redlines: `00_repo/.cbr/reports/editorial/redlines`
- Proposals: `00_repo/.cbr/opportunities/erep/proposals/proposals.json`

## New Gates
- G-EDIT-DIFF · G-EDIT-SCOPE · G-EDIT-APPROVAL · G-EDIT-SOURCE · G-HUMAN-QUALITY

## Use
1) Put JSON at `00_repo/.cbr/erep_policy.json` (replace).
2) Put this MD at `02_Governance/human/EREP_v2.3.2_Editorial_Addendum.md`.
3) Run EREP FULL. Review redlines/proposals, then approve & re-run to apply.
