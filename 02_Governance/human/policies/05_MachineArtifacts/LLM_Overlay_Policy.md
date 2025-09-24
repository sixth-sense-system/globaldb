# LLM Overlay Policy (Discovery/Synthesis Preview)

- Overlay outputs are **preview-only** until accepted via PR.
- Each ticket must include **provenance** (repo path, sha256, line span).
- Acceptance requires reviewer initials and link to the source diff or file section.
- EREP gates must pass before merge: schema validity, coverage, and determinism checks.
- CI exposes artifacts: evidence_tickets.jsonl and rendered views.
- No auto-edit to human files; views regenerate from SSOT only.
- Provider configuration must be set via secure secrets if LLM mode is used.
- Deterministic runs (CONSOLIDATION_ONLY) remain the default on PRs to main.
Generated 2025-09-24T21:04:44Z.
