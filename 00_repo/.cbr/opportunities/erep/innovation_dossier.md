<!-- ERQ-META-BEGIN {"doc_type":"innovation_dossier","spec_version":"2.0","source_baseline_hash":"471210aae34a0cb71fa200aa901d8747e7d0e4f1b6e68781f000f4e17cc22cbb","provenance":{"build_id":"f97e7e0e-c8b6-4c2e-9ea3-8cefafaa40e0","built_at":"2025-09-12T00:40:16Z","builder":"EREP v2.2","tools":{"python":"3.10","hashlib":"sha256"}},"governance_links":{"acceptance_gates":"00_repo/.cbr/acceptance_gates.yaml","registry":"00_repo/.cbr/registry.json","audit_log":"00_repo/.cbr/audit_log.json"},"canonicalization":{"encoding":"utf-8","newline":"LF","sort_keys":true},"integrity":{"algo":"sha256","canonical_scope":"payload","value":"2349123fb899b5a0ecf4faffafa6b1d74c4b2e43401a031c6f484527261e2f89"}} ERQ-META-END -->
# ENERQIS — EREP v2.2 Innovation Dossier

## New Concepts (12)
### NC-02 — Regime‑Aware Risk Kernel (RARK)
**Rank:** 0.791
**Rationale:** Centralize regime detection to scale dynamic position sizing and throttles.
**Modules:** 06_System
**Impacts:** 06_System/machine/experiment_manifest.json, 06_System/machine/parity_logs.json

### NC-01 — Space‑Weather Signal Lattice (SWSL)
**Rank:** 0.765
**Rationale:** Model geomagnetic/solar activity → human behavior → market microstructure pathways.
**Modules:** 08_Market, 06_System, 11_Research
**Impacts:** 08_Market/machine/indicator_configs.yaml, 06_System/machine/experiment_manifest.json, 11_Research/machine/experiments/

### NC-09 — Adaptive Portfolio Throttle (APT)
**Rank:** 0.75
**Rationale:** Capital throttling via drawdown and liquidity‑aware risk constraints.
**Modules:** 06_System, 02_Governance
**Impacts:** 06_System/machine/experiment_manifest.json, 02_Governance/machine/access_control.json

### NC-06 — Drift/Break Detection Watchtower (DBDW)
**Rank:** 0.746
**Rationale:** Stat tests for feature/label drift and structural breaks, with gated rollout.
**Modules:** 03_Data, 06_System
**Impacts:** 03_Data/machine/validation_checks.log, 06_System/machine/experiment_manifest.json

### NC-10 — Data Quality SLA Sentinel (DQSS)
**Rank:** 0.742
**Rationale:** Per‑dataset SLAs; alert and quarantine on breach.
**Modules:** 03_Data
**Impacts:** 03_Data/machine/dataset-manifests/datasets_index.json, 03_Data/machine/validation_checks.log

### NC-12 — Observability‑Everywhere Telemetry Kit (OETK)
**Rank:** 0.732
**Rationale:** Unified logs/metrics/traces with alerts for data & strategy health.
**Modules:** 09_Tech, 13_OpsLog
**Impacts:** 09_Tech/machine/observability_manifest.json, 13_OpsLog/machine/ops_workflows.yaml

### NC-05 — Execution Latency Budgeter (ELB)
**Rank:** 0.731
**Rationale:** Budget and monitor latency across execution path; auto‑adapt order types.
**Modules:** 09_Tech, 06_System
**Impacts:** 09_Tech/machine/observability_manifest.json, 06_System/machine/parity_logs.json

### NC-07 — Cross‑Platform Strategy Parity Harness (CPSPH)
**Rank:** 0.731
**Rationale:** Guarantee equivalence between cBot and Python ref implementations.
**Modules:** 06_System
**Impacts:** 06_System/machine/parity_logs.json, 06_System/machine/experiment_manifest.json

### NC-03 — Shock Propagation Graph (SPG)
**Rank:** 0.729
**Rationale:** Graph of cross‑asset spillovers to inform hedges and stop logic.
**Modules:** 08_Market, 06_System
**Impacts:** 08_Market/machine/instrument_metadata.json, 06_System/machine/system_strategies/

### NC-11 — Provenance‑First Experiment Ledger (PFEL)
**Rank:** 0.724
**Rationale:** Experiments as immutable, queryable ledgers with full lineage.
**Modules:** 11_Research
**Impacts:** 11_Research/machine/experiments/exp_manifest.schema.json, 11_Research/machine/research_index.json

### NC-04 — Narrative‑Sentiment Fusion Index (NSFI)
**Rank:** 0.72
**Rationale:** Combine financial news embeddings and retail sentiment to form meta‑signals.
**Modules:** 10_AI_Algo, 08_Market
**Impacts:** 10_AI_Algo/machine/model_registry.json, 08_Market/machine/research_notes_embeddings.json

### NC-08 — Synthetic Feature Forge (SFF)
**Rank:** 0.698
**Rationale:** Programmatic generation of candidate features with leakage guards.
**Modules:** 03_Data, 11_Research
**Impacts:** 03_Data/machine/schema_registry.json, 11_Research/machine/experiments/

## Additional Opportunities (13)
- **AO-01 — SBOM & Attestation pipeline** (Modules: 09_Tech, 00_repo) — Generate SBOMs and sign release artifacts.
- **AO-02 — Secrets management baseline** (Modules: 04_Infrastructure, 02_Governance) — Vault/KMS integration + rotation SOPs.
- **AO-03 — Dataset dedup fingerprinting** (Modules: 03_Data) — Min‑hash fingerprints for historical datasets.
- **AO-04 — Market calendar oracle** (Modules: 08_Market) — Canonical holidays/events for backtests and live.
- **AO-05 — Regime labeling taxonomy** (Modules: 06_System, 07_Theory) — Common labels and thresholds for regimes.
- **AO-06 — Feature store parquet layout v1** (Modules: 03_Data) — Partitioning/layout conventions for features.
- **AO-07 — Walk‑forward CV runner** (Modules: 11_Research, 06_System) — Reusable WFCV harness with purged CV.
- **AO-08 — Strategy registry with metadata** (Modules: 06_System) — Discoverable catalog of strategies with owners.
- **AO-09 — Auto backtest report generator** (Modules: 06_System) — Deterministic PDF/HTML reports from runs.
- **AO-10 — Research notebook templating** (Modules: 11_Research) — Standardized Jupyter templates linked to exp IDs.
- **AO-11 — Governance proposal auto‑gen** (Modules: 02_Governance, 00_repo) — Open proposals on new paths/features.
- **AO-12 — Risk limits as code** (Modules: 06_System, 02_Governance) — YAML risk configs enforced by CI.
- **AO-13 — DR drill generator** (Modules: 04_Infrastructure, 13_OpsLog) — Quarterly scenario runbooks and checklists.
