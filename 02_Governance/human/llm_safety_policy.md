# ERQ-META-BEGIN
# {"canonicalization": {"encoding": "utf-8", "newline": "LF", "sort_keys": true}, "doc_type": "policy", "governance_links": {"acceptance_gates": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/acceptance_gates.yaml", "audit_log": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/audit_log.json", "registry": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/registry.json"}, "integrity": {"algo": "sha256", "canonical_scope": "payload", "value": "1453d3f805bf95c5e52df9c639579d5b87a543383cc1ab8e3555d8a95cfc210c"}, "provenance": {"build_id": "6583bd07-a0b9-4e6b-8e14-80705575b128", "builder": "EREP v2.2", "built_at": "2025-09-12T02:29:07Z", "tools": {"hashlib": "sha256", "platform": "Linux-4.4.0-x86_64-with-glibc2.36", "python": "3.11.8"}}, "source_baseline_hash": "sha256:a16aa6c5ed17ee977a3aec9f4a0c058be2d9121a693d4247fc8a1853dff10191", "spec_version": "2.0"}
# ERQ-META-END
# ENERQIS — LLM Safety Policy

**Canonical Baseline**

AI systems integrated into ENERQIS must follow strict safety protocols.

## ✦ Rules
1. **Sanitization** — all retrieved LLM outputs filtered for sensitive data.
2. **Provenance Tagging** — every AI-generated artifact annotated with dataset hash, model ID, and seed where applicable.
3. **No Secrets or PII** — sensitive or proprietary data never directly fed to or returned from external LLMs.
4. **Containment** — LLM outputs are advisory until confirmed via synthesis; they do not overwrite canonical files automatically.

This ensures that AI augments governance but cannot bypass it.