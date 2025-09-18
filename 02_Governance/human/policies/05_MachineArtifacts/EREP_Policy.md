# EREP v1.1 — ENERQIS Repository Enforcement & Provenance

**File to add:** `00_repo/.cbr/erep_policy.md` (paste this whole section)

## 1) Purpose

EREP v1.1 guarantees that ENERQIS stays **complete, deterministic, governed, and auditable** as it evolves. It enforces the ERQ-META standard on machine artifacts, validates structure parity against the locked tree, protects human files from truncation/placeholder drift, and generates upgrade overlays when it finds gaps.

## 2) Scope

* Applies to the **entire repository** rooted at `ENERQIS_GlobalDB_TREEBUILD/`.
* Focus checks:
  a) **Structure Parity** vs `00_repo/.cbr/structure_lock.json`
  b) **Human Long-Form Integrity** (verbatim, no placeholders)
  c) **Machine ERQ-META Compliance** (spec/provenance/governance/integrity)
  d) **Crosslink & Schema Validity** (Markdown links + JSON schemas)
  e) **Determinism & Write-scope Gates** (UTC, sorted keys, allowed roots)

## 3) ERQ-META (required for all machine/control artifacts)

Each machine file must carry **spec & provenance** plus integrity, either:

* As a **comment header** for text formats (YAML/TOML/INI/sh), or
* As a top-level `x_erq_meta` for JSON, or
* As a **sidecar** `<file>.meta.json` for binaries (e.g., `.cbot`, `.zip`).

**ERQ-META keys (minimum):**

* `doc_type` (e.g., `workflow`, `manifest`, `config`, `dataset-index`)
* `spec_version` (e.g., `1.0`)
* `source_baseline_hash` (the sealed baseline hash you confirmed)
* `provenance` → `build_id`, `built_at` (UTC ISO-8601), `builder`, `tools {…}`
* `governance_links` → absolute repo paths to:

  * `00_repo/.cbr/acceptance_gates.yaml`
  * `00_repo/.cbr/registry.json`
  * `00_repo/.cbr/audit_log.json`
* `canonicalization` → `{encoding:utf-8, newline:LF, sort_keys:true}`
* `integrity` → `{algo:sha256, canonical_scope:payload, value:<hex>}`

**YAML example (comment header):**

```yaml
# ERQ-META-BEGIN
# {"doc_type":"workflow","spec_version":"1.0","source_baseline_hash":"<BASELINE_HEX>",
#  "provenance":{"build_id":"<uuid>","built_at":"2025-09-10T00:46:55Z","builder":"EREP v1.1","tools":{"python":"3.10","hashlib":"sha256"}},
#  "governance_links":{"acceptance_gates":"00_repo/.cbr/acceptance_gates.yaml","registry":"00_repo/.cbr/registry.json","audit_log":"00_repo/.cbr/audit_log.json"},
#  "canonicalization":{"encoding":"utf-8","newline":"LF","sort_keys":true},
#  "integrity":{"algo":"sha256","canonical_scope":"payload","value":"<HEX>"}}
# ERQ-META-END
```

**JSON example (embedded):**

```json
{
  "x_erq_meta": {
    "doc_type": "manifest",
    "spec_version": "1.0",
    "source_baseline_hash": "<BASELINE_HEX>",
    "provenance": { "build_id": "<uuid>", "built_at": "2025-09-10T00:46:55Z", "builder": "EREP v1.1", "tools": {"python": "3.10"} },
    "governance_links": {
      "acceptance_gates": "00_repo/.cbr/acceptance_gates.yaml",
      "registry": "00_repo/.cbr/registry.json",
      "audit_log": "00_repo/.cbr/audit_log.json"
    },
    "canonicalization": { "encoding": "utf-8", "newline": "LF", "sort_keys": true },
    "integrity": { "algo": "sha256", "canonical_scope": "payload", "value": "<HEX>" }
  },
  "...": "rest of the file"
}
```

**Binary example (sidecar):**

```
06_System/machine/prototype_strategies/cBot_SimpleMA.cbot
06_System/machine/prototype_strategies/cBot_SimpleMA.cbot.meta.json  <-- contains ERQ-META JSON as above
```

## 4) Canonicalization & Integrity

* **Do not rewrite** payloads on disk to pass hashing; canonicalization is a logical view used only for hashing:

  * Text: normalize to UTF-8, LF line endings.
  * JSON: sort keys; remove insignificant whitespace when hashing.
  * Binaries: use raw bytes.
* `integrity.value` must equal `sha256(canonical_payload)`. Failing this is a **hard gate**.

## 5) Human Long-Form Rules

* No placeholders: forbids tokens like `"(omitted for brevity)"`, `"TBD"`, `"<<placeholder>>"`.
* Balanced fences for code blocks.
* Min length guard (default **≥ 200 bytes** except for short policy stubs).
* When EREP flags a human file, fix the source document—not by stuffing bytes.

## 6) Crosslink & Schema Validations

* Resolve relative links in all `*/human/*.md`; 0 broken links allowed by default.
* Validate JSON artifacts against known schemas:

  * `11_Research/machine/experiments/exp_manifest.schema.json`
  * `00_repo/.cbr/provenance_schema.json` for ERQ-META sidecars or embedded objects where applicable.
* Additional module schemas may be referenced in `00_repo/.cbr/acceptance_gates.yaml`.

## 7) Determinism & Write-Scope

* EREP runs with `TZ=UTC` and should assume `SOURCE_DATE_EPOCH` semantics where reproducible builds are used.
* CI must restrict write operations to **allowed roots** (module `/machine` trees + `.cbr/` logs/manifests). Everything else is read-only.

## 8) Outputs

* `out/<stamp>/audit.json` — machine-readable findings (missing, non-compliant, enriched).
* `out/<stamp>/compliance_summary.md` — human summary.
* `out/<stamp>/ENERQIS_ERQ-META_UpgradePack.zip` — overlay to bring lagging artifacts to spec (text ERQ-META headers or binary sidecars).
* Always compute and ship SHA-256 for each emitted artifact.

## 9) Pass/Fail Policy

* **Fail** if: any required path missing vs. `structure_lock.json`, any human placeholder breach, any ERQ-META integrity mismatch, any schema or crosslink error, or any write outside allowed roots.
* **Warn** only for non-critical metadata gaps (e.g., missing optional `tools` versions) if `--warn-metadata` is enabled; default is **strict**.

## 10) Governance & Change Control

* EREP spec lives in `00_repo/.cbr/erep_policy.md` (this file).
* Gate configuration is codified in `00_repo/.cbr/acceptance_gates.yaml` (see below).
* Changes to EREP or gates require PR with label `governance/erep`, 1 approval from `@governance-team`, and a corresponding **audit\_log.json** entry.
