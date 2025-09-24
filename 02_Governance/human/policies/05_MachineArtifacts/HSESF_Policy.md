# HSESF Policy — Hybrid Semantic Extraction & Synthesis Framework
Generated: 2025-09-24T21:17:30Z

## Purpose
Guarantee complete capture of implicit/explicit work and ideas across ENERQIS by
combining deterministic SSOT pipelines with governed semantic overlays (preview-only).

## Scope
- Applies to all runs: OpsLog Consolidation, Discovery, Synthesis, Research ingestion.
- Applies to all modules 00..13 and 99_Archive where human text is present.

## Principles
1. SSOT is authoritative; views are derived. No direct hand edits to derived views.
2. Semantic outputs are preview-only (Evidence Tickets). Promotion requires review & PR.
3. Every preview item must include provenance (repo path, sha256, line span).
4. EREP gates enforce determinism, schema validity, and coverage before merge.
5. Local/CI runs must be reproducible; model usage is optional and pluggable.

## Artifacts
- Evidence Tickets (JSONL) → schema-validated
- SSOT tables (parquet/jsonl): events, decisions, configs, ideas, roadmap, scorecard
- Generated views: HISTORY, DECISIONS, SYSTEMS, EXEC_SCORECARD, NEXT, ROADMAP (+ Mission Control mirror)

## Roles & Approvals
- Owner: 13_OpsLog maintainer (default: @ENERQIS)
- Reviewers: 02_Governance, 05_Blueprint, 06_System code owners
- Required: at least 1 reviewer sign-off for ticket promotion; 2 for changes to policies

## Promotion Rules
- Ticket → Event: factual, verifiable, completed action
- Ticket → Decision: ADR or governance outcome with rationale
- Ticket → Config: controlled parameter or guardrail change (signed if runtime)
- Ticket → Roadmap: actionable, scheduled, with deps & evidence targets
- Ticket → Idea: not ready to schedule; keep origin and confidence

## CI Requirements
- Consolidation runs on PRs (no model). Preview job optional (manual/dispatch).
- Artifacts: opslog-ci (views/validations), opslog-preview (evidence_tickets.jsonl).
- Failing gates block merge.

## Data Retention
- SSOT is cumulative; entries are updated (status, supersession) not deleted.
- Evidence Tickets are kept for 12 months or until promoted/rejected.

## Security
- No model keys stored in repo. Use CI secrets. All actions pinned by SHA.
- sops/age for any secrets; minisign for runtime config signatures.

## Change Control
- Policy changes require PR with changelog, passing EREP gates, and two approvals.
