# ERQ-META-BEGIN
# {"canonicalization": {"encoding": "utf-8", "newline": "LF", "sort_keys": true}, "doc_type": "machine_spec", "governance_links": {"acceptance_gates": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/acceptance_gates.yaml", "audit_log": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/audit_log.json", "registry": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/registry.json"}, "integrity": {"algo": "sha256", "canonical_scope": "payload", "value": "006de72d719baf91ba5af8e453b9d6adb943fb4f22d33d93119e527d57fc2a74"}, "provenance": {"build_id": "54e5cfb2-5908-4fc1-bd8a-c9f16d106ee6", "builder": "EREP v2.2", "built_at": "2025-09-12T02:29:07Z", "tools": {"hashlib": "sha256", "platform": "Linux-4.4.0-x86_64-with-glibc2.36", "python": "3.11.8"}}, "source_baseline_hash": "sha256:a16aa6c5ed17ee977a3aec9f4a0c058be2d9121a693d4247fc8a1853dff10191", "spec_version": "2.0"}
# ERQ-META-END
## 📘 Governance Doc — “Deterministic Machine Artifact Regeneration (RC0)”

**Path (recommended):** `02_Governance/human/policies/RC0_Deterministic_Regen.md`
**Version:** v1.0

### 1) Purpose

Define a deterministic, auditable procedure to regenerate **all machine artifacts** across ENERQIS from canonical **human specs**, yielding production-ready outputs suitable for promotion to a Release Candidate (RC) and, later, a new Baseline.

### 2) Scope

* Modules `00_repo` → `13_OpsLog`, `99_Archive`.
* Artifacts under `**/machine/**`, plus machine-owned infra trees (`templates/`, `tools/`, `ci/`), excluding secrets.

### 3) Inputs

* Canonical human specifications (confirmed `content_human_XX.jsonl` or the live tree matching the sealed baseline).
* Pinned toolchain/containers (see §4).
* Optional: data feeds / fixtures required for data-dependent outputs (see §8 Data Readiness Matrix).

### 4) Deterministic Build Environment (Required)

* **OS/Container:** pinned image; `TZ=UTC`, `LC_ALL=C`, `LANG=C.UTF-8`.
* **Tool versions:** pinned (Python/Node/.NET/CLIs); freeze files committed (`requirements.txt`, lockfiles).
* **Determinism flags:**

  * Fixed random seeds (`SEED=1729` by default)
  * Canonical JSON: **sorted keys**, LF newlines
  * Canonical file order: **sorted path list** for walks/packing
  * Strip or standardize timestamps (`SOURCE_DATE_EPOCH`), or place them in a separate **provenance** block.
* **Rebuild metadata:** embed `{tool_versions, seeds, tz, build_id}` in machine JSON where appropriate.

### 5) Artifact Classes

* **Static machine**: manifests, configs, registries, CI workflows, schemas, templates → **must** reproduce bit-identically.
* **Data-dependent machine**: backtests, experiment logs/results, embeddings, caches → reproduce deterministically **if** inputs are present/pinned; else produce **schema-valid empty** with `data_ready=false`.

### 6) Outputs (Per Module)

* `content_machine_XX.jsonl` — full bytes (UTF-8 or Base64), one record per file.
* `manifest_XX.jsonl` — compact index (no `content`).
* `.cbr/rc/rc_lock.json` — RC fingerprint & metadata.
* `RC_Report_XX.md` — coverage, data readiness, change log.

### 7) Quality Gates (Hard Fail)

* JSONL schema invalid; missing required fields.
* Any `content_machine_XX.jsonl` record whose `sha256(content)` mismatch.
* Non-deterministic JSON (unsorted keys), non-LF newlines, or unstable file order.
* Placeholders (`"omitted for brevity"`, `"..."`, `"[omitted]"`, `"(omitted"`).
* Secrets/PII detected in machine artifacts.
* Data-dependent artifact marked `data_ready=true` with missing inputs or non-reproducible steps.

### 8) Data Readiness Matrix (Examples)

| Artifact                                  | Inputs Required                           | RC0 Behavior if Missing                          |
| ----------------------------------------- | ----------------------------------------- | ------------------------------------------------ |
| `06_System/machine/backtest_results.json` | Historical OHLCV fixture; strategy params | Emit schema-valid `runs: []`, `data_ready=false` |
| `10_AI_Algo/machine/experiment_results/*` | Datasets; seeds; model cfg                | Emit empty results; `data_ready=false`           |
| `11_Research/machine/research_index.json` | Human docs (present)                      | Build fully; `data_ready=true`                   |
| `ci/*` workflows                          | None beyond policy                        | Build fully; deterministic                       |

> RC0 may ship **valid-empty** data-dependent artifacts; RC promotion to Baseline requires a data-ready pass or explicit Governance waiver.

### 9) Procedure

1. **Pin & prepare** env (§4).
2. **Generate** machine artifacts per module from human specs.
3. **Validate** (quality gates §7).
4. **Hashing:** per-file SHA-256 → `manifest_XX.jsonl`; compute **module manifest hash** (sorted canonical form).
5. **RC fingerprint:** compute RC global hash (sorted `<module_id>:<module_manifest_sha256>`); write `.cbr/rc/rc_lock.json`.
6. **Publish RC0 bundle:**

   * `content_machine_XX.jsonl`, `manifest_XX.jsonl` for all modules
   * `.cbr/rc/*`, `RC_Report_*.md`
   * `BaselineBundle_RC0.zip` + `.sha256`

### 10) Promotion

* **RC → Baseline vN** when:

  * All quality gates pass,
  * Data-dependent artifacts are `data_ready=true` (or waived),
  * Operator issues **CONFIRM MODULE <XX> \<manifest\_sha256>** for changed modules,
  * Global hash sealed in `.cbr/global_lock.json`.
* Package `BaselineBundle_vN.zip` + `.sha256`.

### 11) CI Workflow (template)

```yaml
name: RC0 Machine Regeneration
on: [workflow_dispatch]
jobs:
  regen:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v4
        with: { python-version: '3.10' }
      - run: pip install -r ci/requirements.txt
      - name: Build machine artifacts deterministically
        run: python ci/build_machine.py --seed 1729 --tz UTC
      - name: Validate & hash
        run: python ci/validate_and_hash.py --fail-on-any
      - name: Assemble RC0 bundle
        run: python ci/package_rc.py --out packages/
      - uses: actions/upload-artifact@v4
        with:
          name: BaselineBundle_RC0
          path: packages/BaselineBundle_RC0.*
```

### 12) Acceptance Criteria (RC0)

* **Completeness:** Each module has `content_machine_XX.jsonl` + `manifest_XX.jsonl`.
* **Integrity:** `files_ok == 100%`, `sha_mismatch == 0`, `no_placeholders == true`.
* **Determinism:** canonical JSON, LF newlines, stable ordering confirmed.
* **Provenance:** build metadata embedded.
* **Data readiness:** per artifact flag present; RC report lists any `false`.
* **Governance:** RC global hash recorded in `.cbr/rc/rc_lock.json`; operator acknowledges RC0.
