# ERQ-META-BEGIN
# {"canonicalization": {"encoding":"utf-8","newline":"LF","sort_keys": true},
#  "doc_type":"control","spec_version":"2.4",
#  "provenance":{"builder":"EREP v2.4 HardeningPack","built_at":"2025-09-12T19:24:51Z","tools":{"python":"3"}},
#  "governance_links":{"acceptance_gates":"00_repo/.cbr/acceptance_gates.yaml","registry":"00_repo/.cbr/registry.json","audit_log":"00_repo/.cbr/audit_log.json"}}
# ERQ-META-END
# EREP v2.4 — Idempotent FULL (policy mirror)

> Read-only human mirror of `00_repo/.cbr/erep_policy.json`. JSON is the source of truth.


# EREP v2.4.1 — Read-Only MD (drop in at `00_repo/.cbr/erep_policy.md`)

**ERQ-META:**
`# ERQ-META-BEGIN` fenced header is injected into text-like files; JSON uses `_erq_meta` (object) or a single `*.meta.json` sidecar (arrays).

## What’s new in 2.4.1 (Prune & Package)

* **Overlay runs** now **emit a precise delete list** (`erep_delete_list.txt`) + **ready-to-run prune scripts** (`erep_prune.sh` / `erep_prune.ps1`). Nothing is deleted automatically in overlay mode; you have explicit control.

* **Full repo packages** (when you ask us to ship a whole fixed repo) perform **auto-pruning** during packaging:

  * Remove **sidecar chains** (e.g., `*.meta.json.meta.json*`, `*.erqmeta.json`).
  * Remove **redundant sidecars** when the parent already carries fenced or embedded `ERQ-META`.
  * Retain **exactly one** sidecar for **JSON arrays** (arrays can’t embed).
  * **Retain last 5 runs** and any **≥ v2.4 reports**; archive or drop older ones.

* New gate **`G-ERQ-META-UNIQUE`** forbids more than one sidecar per parent.

* Existing gate **`G-EREP-EQUIV`** ensures FULL and COMPLIANCE agree (no flip-flop runs).

## Safety rails

* All pruning honors **structure lock** and **protect\_globs**.
* A JSON and text report are stored at `00_repo/.cbr/reports/erep_prune_report.json` and `erep_delete_list.txt`.
* In overlay mode we never delete automatically—**you** run the script if you agree.
