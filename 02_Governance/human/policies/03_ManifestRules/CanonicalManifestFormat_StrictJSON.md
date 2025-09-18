# ERQ-META-BEGIN
# {"canonicalization": {"encoding": "utf-8", "newline": "LF", "sort_keys": true}, "doc_type": "machine_spec", "governance_links": {"acceptance_gates": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/acceptance_gates.yaml", "audit_log": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/audit_log.json", "registry": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/registry.json"}, "integrity": {"algo": "sha256", "canonical_scope": "payload", "value": "bc917e9f60f7387c18dd23a22c8946b40fd1ef0fb43b4bd7eed2cc414e78e3c1"}, "provenance": {"build_id": "5fef6faf-4fbf-48e3-a919-539833d25b63", "builder": "EREP v2.2", "built_at": "2025-09-12T02:29:07Z", "tools": {"hashlib": "sha256", "platform": "Linux-4.4.0-x86_64-with-glibc2.36", "python": "3.11.8"}}, "source_baseline_hash": "sha256:a16aa6c5ed17ee977a3aec9f4a0c058be2d9121a693d4247fc8a1853dff10191", "spec_version": "2.0"}
# ERQ-META-END
## 🔒 **Canonical Manifest Format Policy**

### 1. Scope

This addendum applies to every module manifest, registry, or snapshot generated inside ENERQIS\_GlobalDB.

### 2. Format

* **Canonical Manifest Format = Strict JSON.**
* Every module, section, and field must be represented as a valid JSON object or array.
* No markdown headings, no comments, no extraneous symbols outside JSON syntax.

### 3. Presentation

* Any time a manifest segment, module, or the full manifest is presented for review or confirmation, it must be output in **this exact JSON format**.
* If a human-readable view is desired, it can be generated separately as a secondary view — but the canonical, locked version is always JSON.

### 4. Locking

* Only the strict JSON version will be hashed, stored, and treated as the “source of truth” for CSEP/CSEL.
* Once confirmed by you with the `CONFIRM MODULE <NN> <manifest-sha256>` phrase, that JSON snapshot is considered immutable.

### 5. Export

* The final export of ENERQIS\_GlobalDB (ZIP or JSON chunks) will be **the strict JSON manifests**.
* These can be re-uploaded to a new chat or environment and will be used verbatim without inference.

---

From this point forward, every manifest segment and the final combined manifest will follow **this strict JSON policy**.
