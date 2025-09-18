# ERQ-META-BEGIN
# {"canonicalization": {"encoding": "utf-8", "newline": "LF", "sort_keys": true}, "doc_type": "machine_spec", "governance_links": {"acceptance_gates": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/acceptance_gates.yaml", "audit_log": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/audit_log.json", "registry": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/registry.json"}, "integrity": {"algo": "sha256", "canonical_scope": "payload", "value": "cd4753113b5ad87f09cf232b271d2e34f8934e5c36073cd2358acccf02e3e29a"}, "provenance": {"build_id": "36dee3cf-a685-472a-acc6-d0aaeb392731", "builder": "EREP v2.2", "built_at": "2025-09-12T02:29:07Z", "tools": {"hashlib": "sha256", "platform": "Linux-4.4.0-x86_64-with-glibc2.36", "python": "3.11.8"}}, "source_baseline_hash": "sha256:a16aa6c5ed17ee977a3aec9f4a0c058be2d9121a693d4247fc8a1853dff10191", "spec_version": "2.0"}
# ERQ-META-END
# Dual-Artifact Packaging & Export Integrity Policy (DAP-EI) — v1.0

**Path (recommend):** `02_Governance/human/policies/DAP-EI.md`
**Applies to:** All modules (`00_repo` → `13_OpsLog`, `99_Archive`)
**Purpose:** Guarantee deterministic **rebuilds/exports** and **auditability** of ENERQIS by separating human and machine bytes, enforcing hash-based integrity, and eliminating placeholders.

---

## 1) Objectives

* **Deterministic rebuilds:** Any third party can reconstruct the repo **byte-for-byte** from JSONL packs + lock files.
* **Operational safety:** Reviews stay fast (small manifests) while full-fidelity packs remain available.
* **No drift:** All exports re-derive per-module and global fingerprints; promotion requires cryptographic confirmation.
* **Zero placeholders:** Canonical artifacts always contain **full content**; no “omitted” text.

---

## 2) Artifact Model (per module XX)

Each module maintains **three** JSONL packs:

1. `content_human_XX.jsonl` — **full human bytes** (UTF-8).
2. `content_machine_XX.jsonl` — **full machine bytes** (Base64 for non-text).
3. `manifest_XX.jsonl` — **compact index** only (paths + hashes + sizes), no `content`.

A **baseline bundle** aggregates all modules:
`BaselineBundle_v{N}.zip` → contains all `content_*_XX.jsonl`, all `manifest_XX.jsonl`, and lock files under `.cbr/`.

---

## 3) Naming & Layout

```
02_Governance/
  human/
    policies/
      DAP-EI.md
.cbr/
  audit_log.json
  registry_status.json
  global_lock.json
  module-manifests/manifest_00.json
  module-manifests/manifest_01.json
  ...
packages/
  BaselineBundle_vN.zip
  BaselineBundle_vN.sha256
```

---

## 4) JSONL Record Schema (canonical)

Each line is a JSON object **one file per line**.

**`content_human_XX.jsonl` / `content_machine_XX.jsonl`:**

```json
{
  "module_id": "06",
  "path": "06_System/machine/backtest_results.json",
  "sha256": "51fef208a744e3942d7baf9757bf2ebcd6dd11362db3f1ddde75b5fa40644858",
  "size_bytes": 12345,
  "mtime_iso8601": "2025-09-08T18:19:07Z",
  "encoding": "utf8 | base64",
  "kind": "human | machine",
  "content": "<full bytes: utf8 text or base64>"
}
```

**`manifest_XX.jsonl`:**

```json
{
  "module_id": "06",
  "path": "06_System/machine/backtest_results.json",
  "sha256": "51fef208a744e3942d7baf9757bf2ebcd6dd11362db3f1ddde75b5fa40644858",
  "size_bytes": 12345,
  "mtime_iso8601": "2025-09-08T18:19:07Z",
  "encoding": "utf8 | base64",
  "kind": "human | machine"
}
```

**Rules**

* `encoding=base64` **required** for any non-UTF-8/binary content.
* **Prohibited markers** in `content`: `"omitted for brevity"`, `"omitted here for brevity"`, `"..."` (policy fails if present).
* All `path` values are **repo-relative** (no `sandbox:` prefixes).

---

## 5) Integrity & Hashing (unchanged from current baseline)

* **File hash:** `sha256(bytes)` of the reconstructed file.
* **Module manifest hash:** SHA-256 of a canonical JSON array of records with fields
  `[path, sha256, size_bytes, encoding, kind]` **sorted by `path`**; keys sorted; LF line breaks.
* **Global project hash:** SHA-256 over newline-separated lines
  `"<module_id>:<module_manifest_sha256>\n"` ordered by `module_id`.
* These definitions preserve compatibility with the existing sealed baseline.

---

## 6) Promotion Workflow (Draft → Baseline vN)

1. **Ingest & Draft**

   * Produce updated `content_human_XX.jsonl` and/or `content_machine_XX.jsonl` for changed modules.
   * Generate `manifest_XX.jsonl` (no `content`).
2. **Validation Gates (mandatory)**

   * Rebuild dry-run from `content_*_XX.jsonl`; verify **100% file SHA match**.
   * **Zero placeholders** gate.
   * Licenses/secrets/PII scan pass.
   * Backtest hygiene (purged CV/walk-forward) where applicable (Module 06/10/11).
3. **CONFIRM tokens**

   * For each changed module: present `CONFIRM MODULE <XX> <manifest_sha256>`; operator signs off.
4. **Compute Global**

   * Recompute **global hash** from module hashes; present value.
5. **Lock & Package**

   * Write `.cbr/global_lock.json`, update `.cbr/registry_status.json`, append `.cbr/audit_log.json`.
   * Build `BaselineBundle_vN.zip` (all `content_*_XX.jsonl`, all `manifest_XX.jsonl`, `.cbr/*`).
   * Emit `BaselineBundle_vN.sha256`.

---

## 7) Export Procedure (Deterministic)

**Input:** Any complete BaselineBundle (`content_*_XX.jsonl` + `manifest_XX.jsonl` + `.cbr/*`).
**Process:**

1. **Preflight:**

   * Ensure all modules present (`00`–`13`, `99`).
   * Ensure **no placeholders** in any `content_*` JSONLs.
2. **Rebuild:**

   * For each record in `content_human_XX.jsonl` & `content_machine_XX.jsonl`:

     * Write `content` → compute `sha256(bytes)` → must equal record’s `sha256`.
3. **Verify:**

   * Derive per-module manifest hash from rebuilt files → must equal recorded value.
   * Derive global hash → must equal `.cbr/global_lock.json`.
4. **Package:**

   * Emit `ENERQIS_FullBaseline_Export.zip` with the full tree + `.cbr/export_manifest.json` and ZIP SHA-256.

**Exporter must:**

* **Fail fast** on placeholders.
* **Report**: `files_ok`, `sha_mismatch`, `no_content` (should be zero in a BaselineBundle).
* Produce **coverage** by module & kind (human/machine).

---

## 8) CI Gate (GitHub Actions template)

```yaml
name: Baseline Promotion
on:
  workflow_dispatch:
  push:
    paths:
      - '**/content_human_*.jsonl'
      - '**/content_machine_*.jsonl'
      - '**/manifest_*.jsonl'
      - '.cbr/**'

jobs:
  validate-and-lock:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Setup Python
        uses: actions/setup-python@v4
        with: { python-version: '3.10' }
      - name: Install deps
        run: pip install -r ci/requirements.txt
      - name: Validate JSONLs (schema + placeholders)
        run: python ci/validate_jsonls.py
      - name: Rebuild + Verify (per-module & global)
        run: python ci/rebuild_and_verify.py --fail-on-mismatch
      - name: Emit BaselineBundle + SHA
        run: python ci/package_baseline.py --out packages/
      - name: Upload artifact
        uses: actions/upload-artifact@v4
        with:
          name: BaselineBundle
          path: |
            packages/BaselineBundle_v*.zip
            packages/BaselineBundle_v*.sha256
```

**Quality Gates (hard fail):**

* Placeholders found in any `content_*` JSONL.
* Any file SHA mismatch on rebuild.
* Module/global hash mismatch.
* License/secret/PII violations.

---

## 9) Acceptance Criteria

* **Completeness:** For changed modules, both `content_*_XX.jsonl` (as applicable) and `manifest_XX.jsonl` are present.
* **Integrity:** Rebuild yields **0 mismatches**, **0 no\_content**, **0 placeholders**.
* **Governance:** `CONFIRM MODULE` tokens recorded; new global hash published in `.cbr/global_lock.json`.
* **Auditability:** BaselineBundle and its `.sha256` stored in `packages/`.

---

## 10) Security & Compliance

* **Secrets:** Never in content packs; use Vault/KMS (Module 04).
* **Licensing:** Each record carries license metadata; non-permissive assets flagged; promotion blocked if unsatisfied.
* **PII:** Disallowed unless explicitly approved in Governance with redaction policy.

---

## 11) Failure Modes & Remedies

* **Missing machine bytes:** Promotion blocked; regenerate `content_machine_XX.jsonl` or include raw files and re-emit JSONL with `content`.
* **Drift from nondeterminism:** Pin seeds, tool versions, timezones; embed reproducibility metadata in machine JSONLs.
* **Oversized packs:** Split `content_machine_XX.jsonl` by subfolders (e.g., `content_machine_06_part1.jsonl`, etc.) and list them in `manifest_XX.jsonl@parts`.

---

## 12) Migration from Pre-Policy Baseline

1. For the current sealed baseline, generate retroactive `content_machine_XX.jsonl` for modules where machine bytes were not captured.
2. Recreate `BaselineBundle_v{N}` with both `content_human_XX.jsonl` and `content_machine_XX.jsonl`.
3. Rebuild & verify; hashes must match existing module/global fingerprints.
4. Publish and store bundle + SHA.

---

## 13) Roles & RACI

* **Owner:** Module `01_MasterControl` (pipeline), `02_Governance` (policy enforcement).
* **Contributors:** Module owners (produce packs), `09_Tech` (tooling), `13_OpsLog` (audit).
* **Approver:** Governance operator (CONFIRM tokens, global lock).

---

## 14) Operator Commands (standard prompts)

* **“Generate human pack for modules X,Y”** → emits `content_human_XX.jsonl`.
* **“Generate machine pack for modules X,Y”** → emits `content_machine_XX.jsonl`.
* **“Emit manifests for modules X,Y”** → emits `manifest_XX.jsonl`.
* **“Rebuild & verify baseline”** → runs deterministic export, prints per-module/global hashes.
* **“Promote modules X,Y”** → produces confirm tokens & locks, builds `BaselineBundle_vN.zip`.

---

## 15) Versioning

* Policy version in this file header.
* Baselines tagged sequentially: `Baseline v1`, `v2`, … with corresponding `BaselineBundle_v{N}.zip`.
* Any change to hashing/serialization requires a **Governance vote** and a **compatibility note**.

---

### Appendix A — Placeholder Sentinel List (must fail CI)

```
"omitted for brevity"
"omitted here for brevity"
"..."
"[omitted]"
"(omitted"
```

### Appendix B — Minimal `ci/validate_jsonls.py` checks (spec)

* Validate JSONL lines parse, required keys exist.
* `content` present in `content_*` packs; **absent** in `manifest_*`.
* No placeholder markers.
* `sha256(content)` equals record `sha256`.

---

**Adoption:**
On merge of this policy into `02_Governance/human/policies/DAP-EI.md`, we immediately begin producing **dual-artifact packs** for any changed modules. The next promotion will ship the first **BaselineBundle** compliant with DAP-EI v1.0.
