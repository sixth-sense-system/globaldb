# ERQ-META-BEGIN
# {"canonicalization": {"encoding": "utf-8", "newline": "LF", "sort_keys": true}, "doc_type": "machine_spec", "governance_links": {"acceptance_gates": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/acceptance_gates.yaml", "audit_log": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/audit_log.json", "registry": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/registry.json"}, "integrity": {"algo": "sha256", "canonical_scope": "payload", "value": "a3bc5155e463eb7ae73578875d72e3fb2d777d68a8093fbafab1263fc50f5124"}, "provenance": {"build_id": "58c93ede-57ed-4977-941f-a2c4fbb2d288", "builder": "EREP v2.2", "built_at": "2025-09-12T02:29:07Z", "tools": {"hashlib": "sha256", "platform": "Linux-4.4.0-x86_64-with-glibc2.36", "python": "3.11.8"}}, "source_baseline_hash": "sha256:a16aa6c5ed17ee977a3aec9f4a0c058be2d9121a693d4247fc8a1853dff10191", "spec_version": "2.0"}
# ERQ-META-END
# ENERQIS Research & Ingestion Protocol — ERIP v1.1 (Enhanced)

## Purpose

ERIP v1.1 turns **any** ingestion (files, links, autonomous research) into **evidence-backed, implementation-ready upgrades** to ENERQIS—driving strategy innovation, system improvements, and canonical knowledge growth. It guarantees:

* **Depth, rigor, and actionability** (not summaries—deployment-grade outputs).
* **Traceability and reproducibility** (cryptographic provenance).
* **Compounding memory across time** (retrosynthesis joins new and old insights).
* **Immediate integration** into the GlobalDB (with promotion gates to new baselines).

---

## Core Principles

1. **Depth > breadth**: full text, math, code, tables, figures—no shortcuts.
2. **Evidence-first**: every claim tied to a source, confidence score, and fingerprint.
3. **Action bias**: every batch yields strategy specs, code skeletons, backtest plans, and system upgrades.
4. **No drift**: verifiable hashes; changes gated via module confirm → global lock.
5. **Compound memory**: new inputs are stitched into a persistent knowledge fabric; we re-scan the past when the future arrives (retrosynthesis).
6. **Explore adjacent**: allocate budget to “likely-useful but non-obvious” tangents that can unlock outsized edge.

---

## Architecture (“Knowledge Fabric”)

* **Vector Store** (doc/para/sent embeddings) for semantic retrieval.
* **Relational/Columnar Store** (SQLite/DuckDB/Parquet) for structured facts: claims, entities, datasets, metrics, code refs.
* **Knowledge Graph (KG)** of **Entities–Claims–Evidence–Artifacts–Regimes–Strategies** with timestamps & module links.
* **Retrosynthesis Engine**: when new evidence lands, it auto-scans the corpus to **connect backward in time**, reopening shelved ideas and creating **cross-year insights**.
* **Provenance Layer**: per-item SHA-256; source ranking rubric; license/compliance tags.

---

## Workflow (13 Stages)

### 0) Intake Setup

* Create/refresh:
  `03_Data/{raw,processed,derived}`,
  `11_Research/{human,machine}`,
  `11_Research/machine/ingestion_manifest.jsonl` (one row per item).
* Tools: `pdftotext`, LibreOffice, OCR (Tesseract), HTML cleaner, code parsers.

### 1) Multi-Source Ingestion (Files/Links/Autonomous)

* **Files ZIP**: unpack → enumerate → hash (SHA-256).
* **Links**: fetch HTML/PDF; for hubs, capture **top 20** nested links by relevance.
* **Autonomous**: targeted web research aligned to ENERQIS themes (quality rubric below).

### 2) Parsing & Extraction

* PDFs/DOCX/SRT/Images/HTML → full text + page/offset spans.
* Extract tables (Camelot/tabula), formulas (LaTeX/inline), figures (with alt-text).
* For code repos: readme, licenses, src dirs, examples, tests.

### 3) Normalization & Provenance

* Canonical names, sizes, MIME, encodings, DOIs/URLs.
* Compute SHA-256 **of original** and **of extracted text**.
* License & usage flags; release dates; author/venue.

### 4) Indexing & Enrichment

* Multi-granularity embeddings (doc/section/sentence).
* Entity extraction & linking (tickers, assets, indicators, models, datasets).
* Regime tags; latency class; feature families; method taxonomies.
* Persist to Vector DB + Parquet/SQLite.

### 5) Source Evaluation & Ranking

* **Tier 1**: peer-reviewed papers/standards; **Tier 2**: preprints/industry whitepapers; **Tier 3**: code repos with tests; **Tier 4**: reputable blogs; **Tier 5**: forums.
* Score (0–1): **credibility**, **recency**, **reproducibility**, **transferability** to ENERQIS.
* Auto-downrank sources with contradictions absent evidence or poor methodology.

### 6) Understanding & Evidence Modeling

* For each item: **topic, claims, methods, datasets, results, uncertainty, caveats**.
* Attach **confidence** and **supporting quotations/spans**, with offsets/citations.
* Detect conflicts; note missing data; propose minimal experiments to resolve.

### 7) ENERQIS Alignment (Module Mapping)

* Map insights to **06 System, 07 Theory, 08 Market, 09 Tech, 10 AI\_Algo, 11 Research**.
* Identify **candidate signals/features/datasets**, **strategy patterns**, **risk overlays**, **infra changes**.

### 8) Strategy & System Proposals (Multiple Variants)

Each proposal includes:

* **Spec** (objective, markets, horizon, latency, features/signals, rules).
* **Risk** (stops/targets, risk targeting, exposure budgets, clustering).
* **Data** (sources, granularities, survivorship/holiday rules, alignment).
* **Backtest Plan** (windows, purged CV with embargo, walk-forward, IS/OOS split).
* **Metrics** (CAGR, Sharpe/Sortino, tail-risk, drawdown, turnover, slippage).
* **Code**: cBot class skeleton + Python module outline + pseudocode.
* **Monitoring**: anomaly thresholds, alerts, playbooks.

### 9) Experiment Design & Backtests

* **Leakage guards**: time-ordered split; purged K-fold with embargo.
* **Robustness**: sub-periods, regime stratification, parameter stress, data vendor A/B.
* **Microstructure realism**: spread, slippage, latency, partial fills.
* **Parities**: cTrader vs. Python parity checks; reproducible seeds.

### 10) Synthesis Report (Human + Machine)

* Sections: Executive, Per-Item Summaries, Cross-Source Synthesis, Contradictions, ENERQIS Mapping, Strategy Proposals (≥3), Backtest & Data Plan, Gaps/Next Steps, Glossary/Index.
* Machine artifacts: `research_index.json`, vector IDs, KG diffs.

### 11) Draft → Canonical Updates

* Draft updates to `human/*draft*.md` and structured `machine/*`.
* Operator review; upon approval: update canonical `human/*.md`.
* Regenerate **per-module content\_XX.jsonl** for changed modules.

### 12) Promotion & Baseline Re-Seal

* Present new **CONFIRM MODULE <id> <hash>** tokens for changed modules.
* Compute new **Global Project SHA-256**; write `global_lock.json`.
* Append to `audit_log.json`, update `registry_status.json`.
* Package “Baseline vN Lock Files” bundle for archival.

### 13) Retrosynthesis & Feedback Loops

* New content triggers retrospective cross-linking across **all prior years**.
* Open “Insight Tasks” for high-potential joins (e.g., old theory + new data).
* Feed **live telemetry & backtests** back into KG with **hypothesis status** (supported/refuted/uncertain).

---

## Acceptance Criteria & Quality Gates

### Ingestion & Extraction

* 100% of items processed or **explicitly** flagged (paywall, corrupted, unsupported).
* OCR coverage ≥ **99%** of pages, with table capture or image+alt fallback.
* Each item has **two SHA-256s** (original, extracted).

### Source Quality

* Mean source credibility score ≥ **0.70**; Tiers 1–3 constitute ≥ **70%** of citations for major claims.
* Conflicts identified with **proposed tests** to adjudicate.

### Strategy Readiness

* ≥ **3** distinct strategy variants per major idea (diversity of core logic).
* Each variant has **full spec, code skeletons, backtest plan, monitoring**.
* Backtests use **purged CV + embargo** or **walk-forward**; no lookahead/leakage.

### Reproducibility

* Exact commands/params to regenerate extraction and experiments are recorded.
* cTrader–Python parity diffs ≤ **epsilon** on benchmark slice (document epsilon).

### Governance Promotion

* Only changed modules re-confirmed; all confirm tokens recorded.
* New global hash computed and stored; lock files packaged.

---

## Operational Commands (Chat Macros)

**INGEST ZIP**

> “Ingest ZIP `<file>` under ERIP v1.1; extract ➜ OCR ➜ parse tables & formulas; build File DB; embeddings; KG; full synthesis; strategy proposals; backtest plan; module mapping; deliver drafts and confirm tokens for any canonical updates.”

**INGEST LINKS**

> “Ingest links in `<links.txt|csv>`; crawl nested (≤20/hub); apply ERIP v1.1; deliver synthesis + strategy proposals; promotion recommendations.”

**RESEARCH TOPIC**

> “Autonomous research on `<topic>` aligned to ENERQIS; Tier-1 sources prioritized; produce synthesis + strategies + infra changes; cite and score sources.”

**INCUBATE STRATEGIES**

> “From latest synthesis, generate ≥5 strategy families with specs, code skeletons, and backtest plans; rank by expected edge, complexity, and latency.”

**RUN BACKTESTS**

> “Design and run backtests per spec (purged CV or walk-forward); record metrics; parity vs. cTrader; write machine artifacts.”

**PROMOTE MODULES**

> “Promote modules `<ids>`; regenerate per-module JSONLs; present CONFIRM tokens; compute new Global SHA; update lock files.”

**RETROSYNTHESIZE**

> “Run KG retrosynthesis on all prior content; surface cross-year joins, reopened hypotheses, and high-value follow-ups.”

**SECURITY & LICENSE CHECK**

> “Audit ingestion set for license usage/permitted scope; tag and quarantine non-compliant items; propose mitigation.”

---

## Data Models (condensed)

**File DB Entry** (unchanged structure; add compliance & score fields)

```json
{
  "id":"F-20250909-00123",
  "path_or_url":"03_Data/raw/paper_xyz.pdf",
  "sha256":{"original":"...", "extracted":"..."},
  "type":"pdf|docx|image|srt|txt|html",
  "metadata":{"title":"...", "authors":["..."], "date":"YYYY-MM-DD", "venue":"...", "license":"..."},
  "topics":["microstructure","trend-following"],
  "claims":[{"text":"...", "evidence":"span_ref", "confidence":0.83, "citations":["doi:..."], "tier":1}],
  "methods":["HMM","GARCH"],
  "results":{"alpha":"...", "pvalues":"..."},
  "datasets":["tick EURUSD 2015-2024"],
  "regime":["high-vol"],
  "limitations":["small sample"],
  "embeddings":{"doc_vector_id":"vec_..."},
  "quality":{"credibility":0.8,"recency":0.7,"repro":0.6,"transfer":0.9},
  "compliance":{"license_ok":true,"pii":false},
  "created_utc":"..."
}
```

**Strategy Spec** (as given earlier; unchanged—production-ready)

**KG Edge Examples**

* `source -> supports -> claim`
* `claim -> informs -> strategy`
* `result -> contradicts -> prior_claim`
* `dataset -> enables -> backtest_spec`
* `telemetry_metric -> refutes -> hypothesis`

---

## Source Selection Rubric (Browsing/Autonomous)

1. Start with **Tier-1/2** (peer-reviewed, standards, authoritative whitepapers).
2. Add **Tier-3** repos **only** if: active maintenance, tests/examples, permissive license.
3. Use **Tier-4/5** sparingly; require cross-validation with higher tiers.
4. Prefer sources with **data & code** that can be reproduced or inspected.
5. Always capture **dates**; discount stale results in fast-moving domains.

---

## Risk, Compliance, and Safety

* **Licensing**: flag non-permissive; keep quarantined; propose alternatives.
* **PII & sensitive data**: exclude or redact.
* **Operational security**: no secrets in artifacts; use Vault/KMS for credentials.
* **Statistical hygiene**: no p-hacking; preregister tests; separate IS/OOS; document all choices.

---

## KPIs & Dashboards

* Ingestion throughput; % OCR coverage; % Tier-1/2 sources.
* # Strategy families proposed; # promoted; % surviving OOS.
* Parity error distribution; latency/turnover drift; risk violations.
* Retrosynthesis hits per batch; reopened hypotheses resolved.
