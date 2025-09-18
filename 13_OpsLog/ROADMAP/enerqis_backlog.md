# ENERQIS Backlog (v2) — normalized & prioritized
_Generated 2025-09-15 00:41 — ranked by Priority→RICE; includes explainer, benefits, integration speed, complexity._


## CAPTURE (latest) — 2025-09-15

CAPTURE: [Security]|Task|P0|Adopt sops/age secrets with .sops.yaml; encrypt .env.enc; rotate any exposed tokens
CAPTURE: [CI]|Task|P0|Pin GitHub Actions by commit SHA; enable CodeQL + Dependabot (security+versions)
CAPTURE: [Execution]|Task|P0|Implement shared risk module (kill-switch, daily loss cap, position caps) and wire into all cBots
CAPTURE: [Integrity]|Task|P0|Minisign config signing; verify at runtime (block on invalid signature)
CAPTURE: [IIS]|Task|P0|Enable OCR (Tesseract+pytesseract); set G-IIS-OCR-REQUIRED to error
CAPTURE: [Policy]|Task|P0|Add LLM usage policy (no proprietary code to public endpoints; redaction; local-only for sensitive)
CAPTURE: [EREP]|Task|P1|Add code gates (build/style/risk/backtest) and overlays CODE:build:v1
CAPTURE: [Data]|Task|P1|Emit SBOM (CycloneDX) + hash manifest on snapshots; gate G-ARTIFACT-HASH
CAPTURE: [NOESIS]|Task|P1|Add alerts: loss_cap_trip, slippage_3σ, gate_fail; wire execution mark-out telemetry
CAPTURE: [Legal]|Task|P1|Add NDA + IP Assignment templates; start ENERQIS/NOESIS trademark search


--



## Next
### P2
#### #1 — (Near) Counterfactual & causal checks  _(General · Task · P2)_
**Status/Stage:** Inbox / Idea • **Owner:** ENERQIS • **RICE:** 9.8 (R=6.0, I=7.0, C=0.7, E=3.0)  
**When:** start  • due   • **Integration speed:** Next (2–6w) • **Complexity:** Easy
**Explainer** — Imagine: (Near) Counterfactual & causal checks in NOESIS and the Engine.
**Tags** — `causal`
**Notes** — Parsed card in top AI implementations.txt

#### #2 — (Near) Post-Trade Learning Loop  _(General · Task · P2)_
**Status/Stage:** Inbox / Idea • **Owner:** ENERQIS • **RICE:** 9.8 (R=6.0, I=7.0, C=0.7, E=3.0)  
**When:** start  • due   • **Integration speed:** Next (2–6w) • **Complexity:** Easy
**Explainer** — Imagine: (Near) Post-Trade Learning Loop in NOESIS and the Engine.
**Notes** — Parsed card in top AI implementations.txt

#### #3 — (Near) Reasoning-budget search  _(General · Task · P2)_
**Status/Stage:** Inbox / Idea • **Owner:** ENERQIS • **RICE:** 9.8 (R=6.0, I=7.0, C=0.7, E=3.0)  
**When:** start  • due   • **Integration speed:** Next (2–6w) • **Complexity:** Easy
**Explainer** — Imagine: (Near) Reasoning-budget search in NOESIS and the Engine.
**Notes** — Parsed card in top AI implementations.txt

#### #4 — (Now) Dual-System Execution (fast/slow)  _(General · Task · P2)_
**Status/Stage:** Inbox / Idea • **Owner:** ENERQIS • **RICE:** 9.8 (R=6.0, I=7.0, C=0.7, E=3.0)  
**When:** start  • due   • **Integration speed:** Next (2–6w) • **Complexity:** Easy
**Explainer** — Imagine: (Now) Dual-System Execution (fast/slow) in NOESIS and the Engine.
**Notes** — Parsed card in top AI implementations.txt

#### #5 — (Now) Prediction-Market Priors  _(General · Task · P2)_
**Status/Stage:** Inbox / Idea • **Owner:** ENERQIS • **RICE:** 9.8 (R=6.0, I=7.0, C=0.7, E=3.0)  
**When:** start  • due   • **Integration speed:** Next (2–6w) • **Complexity:** Easy
**Explainer** — Imagine: (Now) Prediction-Market Priors in NOESIS and the Engine.
**Notes** — Parsed card in top AI implementations.txt

#### #6 — (Now) Spec-driven, agentic Strategy Factory  _(General · Task · P2)_
**Status/Stage:** Inbox / Idea • **Owner:** ENERQIS • **RICE:** 9.8 (R=6.0, I=7.0, C=0.7, E=3.0)  
**When:** start  • due   • **Integration speed:** Next (2–6w) • **Complexity:** Easy
**Explainer** — Imagine: (Now) Spec-driven, agentic Strategy Factory in NOESIS and the Engine.
**Tags** — `agentic,options`
**Notes** — Parsed card in top AI implementations.txt

#### #7 — 1) Complement-sum & mispricing monitor (binary “YES/NO”)  _(General · Task · P2)_
**Status/Stage:** Inbox / Idea • **Owner:** ENERQIS • **RICE:** 9.8 (R=6.0, I=7.0, C=0.7, E=3.0)  
**When:** start  • due   • **Integration speed:** Next (2–6w) • **Complexity:** Easy
**Explainer** — Imagine: 1) Complement-sum & mispricing monitor (binary “YES/NO”) in NOESIS and the Engine.
**Notes** — Parsed card in next level ideas.md

#### #8 — 1) Whale positioning & flows (on-chain + CEX)  _(General · Task · P2)_
**Status/Stage:** Inbox / Idea • **Owner:** ENERQIS • **RICE:** 9.8 (R=6.0, I=7.0, C=0.7, E=3.0)  
**When:** start  • due   • **Integration speed:** Next (2–6w) • **Complexity:** Easy
**Explainer** — Imagine: 1) Whale positioning & flows (on-chain + CEX) in NOESIS and the Engine.
**Notes** — Parsed card in next level ideas.md

#### #9 — 10) Venue lead–lag & price discovery share  _(General · Task · P2)_
**Status/Stage:** Inbox / Idea • **Owner:** ENERQIS • **RICE:** 9.8 (R=6.0, I=7.0, C=0.7, E=3.0)  
**When:** start  • due   • **Integration speed:** Next (2–6w) • **Complexity:** Easy
**Explainer** — Imagine: 10) Venue lead–lag & price discovery share in NOESIS and the Engine.
**Notes** — Parsed card in next level ideas.md

#### #10 — 10) “Gamma wall” analogs from AMM curvature  _(General · Task · P2)_
**Status/Stage:** Inbox / Idea • **Owner:** ENERQIS • **RICE:** 9.8 (R=6.0, I=7.0, C=0.7, E=3.0)  
**When:** start  • due   • **Integration speed:** Next (2–6w) • **Complexity:** Easy
**Explainer** — Imagine: 10) “Gamma wall” analogs from AMM curvature in NOESIS and the Engine.
**Tags** — `manifold,options`
**Notes** — Parsed card in next level ideas.md

#### #11 — 11) Basis triangles & funding arbitrage diagnostics  _(General · Task · P2)_
**Status/Stage:** Inbox / Idea • **Owner:** ENERQIS • **RICE:** 9.8 (R=6.0, I=7.0, C=0.7, E=3.0)  
**When:** start  • due   • **Integration speed:** Next (2–6w) • **Complexity:** Easy
**Explainer** — Imagine: 11) Basis triangles & funding arbitrage diagnostics in NOESIS and the Engine.
**Notes** — Parsed card in next level ideas.md

#### #12 — 11) Binaries to log-odds & Bayesian updates  _(General · Task · P2)_
**Status/Stage:** Inbox / Idea • **Owner:** ENERQIS • **RICE:** 9.8 (R=6.0, I=7.0, C=0.7, E=3.0)  
**When:** start  • due   • **Integration speed:** Next (2–6w) • **Complexity:** Easy
**Explainer** — Imagine: 11) Binaries to log-odds & Bayesian updates in NOESIS and the Engine.
**Notes** — Parsed card in next level ideas.md

#### #13 — 12) Ambiguity & invalidation arb  _(General · Task · P2)_
**Status/Stage:** Inbox / Idea • **Owner:** ENERQIS • **RICE:** 9.8 (R=6.0, I=7.0, C=0.7, E=3.0)  
**When:** start  • due   • **Integration speed:** Next (2–6w) • **Complexity:** Easy
**Explainer** — Imagine: 12) Ambiguity & invalidation arb in NOESIS and the Engine.
**Tags** — `dashboard`
**Notes** — Parsed card in next level ideas.md

#### #14 — 12) Fiat & macro plumbing hooks  _(General · Task · P2)_
**Status/Stage:** Inbox / Idea • **Owner:** ENERQIS • **RICE:** 9.8 (R=6.0, I=7.0, C=0.7, E=3.0)  
**When:** start  • due   • **Integration speed:** Next (2–6w) • **Complexity:** Easy
**Explainer** — Imagine: 12) Fiat & macro plumbing hooks in NOESIS and the Engine.
**Tags** — `macro`
**Notes** — Parsed card in next level ideas.md

#### #15 — 13) Calendar & rule-change risk  _(General · Task · P2)_
**Status/Stage:** Inbox / Idea • **Owner:** ENERQIS • **RICE:** 9.8 (R=6.0, I=7.0, C=0.7, E=3.0)  
**When:** start  • due   • **Integration speed:** Next (2–6w) • **Complexity:** Easy
**Explainer** — Imagine: 13) Calendar & rule-change risk in NOESIS and the Engine.
**Tags** — `risk`
**Notes** — Parsed card in next level ideas.md

#### #16 — 13) Developer activity & protocol vitality  _(General · Task · P2)_
**Status/Stage:** Inbox / Idea • **Owner:** ENERQIS • **RICE:** 9.8 (R=6.0, I=7.0, C=0.7, E=3.0)  
**When:** start  • due   • **Integration speed:** Next (2–6w) • **Complexity:** Easy
**Explainer** — Imagine: 13) Developer activity & protocol vitality in NOESIS and the Engine.
**Tags** — `options`
**Notes** — Parsed card in next level ideas.md

#### #17 — 14) Lending/borrowing & AMM metrics  _(General · Task · P2)_
**Status/Stage:** Inbox / Idea • **Owner:** ENERQIS • **RICE:** 9.8 (R=6.0, I=7.0, C=0.7, E=3.0)  
**When:** start  • due   • **Integration speed:** Next (2–6w) • **Complexity:** Easy
**Explainer** — Imagine: 14) Lending/borrowing & AMM metrics in NOESIS and the Engine.
**Notes** — Parsed card in next level ideas.md

#### #18 — 14) Macro & survey bridges  _(General · Task · P2)_
**Status/Stage:** Inbox / Idea • **Owner:** ENERQIS • **RICE:** 9.8 (R=6.0, I=7.0, C=0.7, E=3.0)  
**When:** start  • due   • **Integration speed:** Next (2–6w) • **Complexity:** Easy
**Explainer** — Imagine: 14) Macro & survey bridges in NOESIS and the Engine.
**Tags** — `macro`
**Notes** — Parsed card in next level ideas.md

#### #19 — 15) Event families & hierarchical consistency  _(General · Task · P2)_
**Status/Stage:** Inbox / Idea • **Owner:** ENERQIS • **RICE:** 9.8 (R=6.0, I=7.0, C=0.7, E=3.0)  
**When:** start  • due   • **Integration speed:** Next (2–6w) • **Complexity:** Easy
**Explainer** — Imagine: 15) Event families & hierarchical consistency in NOESIS and the Engine.
**Notes** — Parsed card in next level ideas.md

#### #20 — 15) Post-trade mark-out & venue scorecard  _(General · Task · P2)_
**Status/Stage:** Inbox / Idea • **Owner:** ENERQIS • **RICE:** 9.8 (R=6.0, I=7.0, C=0.7, E=3.0)  
**When:** start  • due   • **Integration speed:** Next (2–6w) • **Complexity:** Easy
**Explainer** — Imagine: 15) Post-trade mark-out & venue scorecard in NOESIS and the Engine.
**Tags** — `execution`
**Notes** — Parsed card in next level ideas.md

#### #21 — 2) Cross-venue parity & triangular consistency  _(General · Task · P2)_
**Status/Stage:** Inbox / Idea • **Owner:** ENERQIS • **RICE:** 9.8 (R=6.0, I=7.0, C=0.7, E=3.0)  
**When:** start  • due   • **Integration speed:** Next (2–6w) • **Complexity:** Easy
**Explainer** — Imagine: 2) Cross-venue parity & triangular consistency in NOESIS and the Engine.
**Notes** — Parsed card in next level ideas.md

#### #22 — 2) Liquidation zones / liquidation density  _(General · Task · P2)_
**Status/Stage:** Inbox / Idea • **Owner:** ENERQIS • **RICE:** 9.8 (R=6.0, I=7.0, C=0.7, E=3.0)  
**When:** start  • due   • **Integration speed:** Next (2–6w) • **Complexity:** Medium
**Explainer** — Imagine: 2) Liquidation zones / liquidation density in NOESIS and the Engine.
**Tags** — `dashboard,orderflow`
**Notes** — Parsed card in next level ideas.md

#### #23 — 3) Derivatives positioning (funding, OI, basis)  _(General · Task · P2)_
**Status/Stage:** Inbox / Idea • **Owner:** ENERQIS • **RICE:** 9.8 (R=6.0, I=7.0, C=0.7, E=3.0)  
**When:** start  • due   • **Integration speed:** Next (2–6w) • **Complexity:** Easy
**Explainer** — Imagine: 3) Derivatives positioning (funding, OI, basis) in NOESIS and the Engine.
**Tags** — `options`
**Notes** — Parsed card in next level ideas.md

#### #24 — 3) Time-skew / carry trades  _(General · Task · P2)_
**Status/Stage:** Inbox / Idea • **Owner:** ENERQIS • **RICE:** 9.8 (R=6.0, I=7.0, C=0.7, E=3.0)  
**When:** start  • due   • **Integration speed:** Next (2–6w) • **Complexity:** Easy
**Explainer** — Imagine: 3) Time-skew / carry trades in NOESIS and the Engine.
**Tags** — `options`
**Notes** — Parsed card in next level ideas.md

#### #25 — 4) Options surface & dealer positioning (crypto)  _(General · Task · P2)_
**Status/Stage:** Inbox / Idea • **Owner:** ENERQIS • **RICE:** 9.8 (R=6.0, I=7.0, C=0.7, E=3.0)  
**When:** start  • due   • **Integration speed:** Next (2–6w) • **Complexity:** Easy
**Explainer** — Imagine: 4) Options surface & dealer positioning (crypto) in NOESIS and the Engine.
**Tags** — `options`
**Notes** — Parsed card in next level ideas.md

#### #26 — 4) Order-path slippage & optimal slicing  _(General · Task · P2)_
**Status/Stage:** Inbox / Idea • **Owner:** ENERQIS • **RICE:** 9.8 (R=6.0, I=7.0, C=0.7, E=3.0)  
**When:** start  • due   • **Integration speed:** Next (2–6w) • **Complexity:** Easy
**Explainer** — Imagine: 4) Order-path slippage & optimal slicing in NOESIS and the Engine.
**Tags** — `execution`
**Notes** — Parsed card in next level ideas.md

#### #27 — 5) Resolution-source watcher (machine-read the rulebook)  _(General · Task · P2)_
**Status/Stage:** Inbox / Idea • **Owner:** ENERQIS • **RICE:** 9.8 (R=6.0, I=7.0, C=0.7, E=3.0)  
**When:** start  • due   • **Integration speed:** Next (2–6w) • **Complexity:** Easy
**Explainer** — Imagine: 5) Resolution-source watcher (machine-read the rulebook) in NOESIS and the Engine.
**Tags** — `orderflow`
**Notes** — Parsed card in next level ideas.md

#### #28 — 5) Stablecoin plumbing  _(General · Task · P2)_
**Status/Stage:** Inbox / Idea • **Owner:** ENERQIS • **RICE:** 9.8 (R=6.0, I=7.0, C=0.7, E=3.0)  
**When:** start  • due   • **Integration speed:** Next (2–6w) • **Complexity:** Easy
**Explainer** — Imagine: 5) Stablecoin plumbing in NOESIS and the Engine.
**Tags** — `options`
**Notes** — Parsed card in next level ideas.md

#### #29 — 6) Domain-specific live feeds  _(General · Task · P2)_
**Status/Stage:** Inbox / Idea • **Owner:** ENERQIS • **RICE:** 9.8 (R=6.0, I=7.0, C=0.7, E=3.0)  
**When:** start  • due   • **Integration speed:** Next (2–6w) • **Complexity:** Easy
**Explainer** — Imagine: 6) Domain-specific live feeds in NOESIS and the Engine.
**Tags** — `options`
**Notes** — Parsed card in next level ideas.md

#### #30 — 6) Level-2 (LOB) features & toxicity  _(General · Task · P2)_
**Status/Stage:** Inbox / Idea • **Owner:** ENERQIS • **RICE:** 9.8 (R=6.0, I=7.0, C=0.7, E=3.0)  
**When:** start  • due   • **Integration speed:** Next (2–6w) • **Complexity:** Easy
**Explainer** — Imagine: 6) Level-2 (LOB) features & toxicity in NOESIS and the Engine.
**Tags** — `orderflow`
**Notes** — Parsed card in next level ideas.md

#### #31 — 7) **Cumulative Volume Delta (CVD)** & footprint variants  _(General · Task · P2)_
**Status/Stage:** Inbox / Idea • **Owner:** ENERQIS • **RICE:** 9.8 (R=6.0, I=7.0, C=0.7, E=3.0)  
**When:** start  • due   • **Integration speed:** Next (2–6w) • **Complexity:** Medium
**Explainer** — Imagine: 7) **Cumulative Volume Delta (CVD)** & footprint variants in NOESIS and the Engine.
**Tags** — `options,orderflow`
**Notes** — Parsed card in next level ideas.md

#### #32 — 7) Expert cohort signals  _(General · Task · P2)_
**Status/Stage:** Inbox / Idea • **Owner:** ENERQIS • **RICE:** 9.8 (R=6.0, I=7.0, C=0.7, E=3.0)  
**When:** start  • due   • **Integration speed:** Next (2–6w) • **Complexity:** Easy
**Explainer** — Imagine: 7) Expert cohort signals in NOESIS and the Engine.
**Notes** — Parsed card in next level ideas.md

#### #33 — 8) Iceberg/spoof detection & replenishment  _(General · Task · P2)_
**Status/Stage:** Inbox / Idea • **Owner:** ENERQIS • **RICE:** 9.8 (R=6.0, I=7.0, C=0.7, E=3.0)  
**When:** start  • due   • **Integration speed:** Next (2–6w) • **Complexity:** Easy
**Explainer** — Imagine: 8) Iceberg/spoof detection & replenishment in NOESIS and the Engine.
**Tags** — `execution`
**Notes** — Parsed card in next level ideas.md

#### #34 — 8) Whale & cohort flow (prediction-market edition)  _(General · Task · P2)_
**Status/Stage:** Inbox / Idea • **Owner:** ENERQIS • **RICE:** 9.8 (R=6.0, I=7.0, C=0.7, E=3.0)  
**When:** start  • due   • **Integration speed:** Next (2–6w) • **Complexity:** Easy
**Explainer** — Imagine: 8) Whale & cohort flow (prediction-market edition) in NOESIS and the Engine.
**Notes** — Parsed card in next level ideas.md

#### #35 — 9) Liquidity & inventory pressure  _(General · Task · P2)_
**Status/Stage:** Inbox / Idea • **Owner:** ENERQIS • **RICE:** 9.8 (R=6.0, I=7.0, C=0.7, E=3.0)  
**When:** start  • due   • **Integration speed:** Next (2–6w) • **Complexity:** Easy
**Explainer** — Imagine: 9) Liquidity & inventory pressure in NOESIS and the Engine.
**Tags** — `dashboard`
**Notes** — Parsed card in next level ideas.md

#### #36 — 9) Liquidity regime panel  _(General · Task · P2)_
**Status/Stage:** Inbox / Idea • **Owner:** ENERQIS • **RICE:** 9.8 (R=6.0, I=7.0, C=0.7, E=3.0)  
**When:** start  • due   • **Integration speed:** Next (2–6w) • **Complexity:** Easy
**Explainer** — Imagine: 9) Liquidity regime panel in NOESIS and the Engine.
**Tags** — `dashboard,manifold`
**Notes** — Parsed card in next level ideas.md

#### #37 — A simple “Top Projects” watchlist you can act on  _(General · Task · P2)_
**Status/Stage:** Inbox / Idea • **Owner:** ENERQIS • **RICE:** 9.8 (R=6.0, I=7.0, C=0.7, E=3.0)  
**When:** start  • due   • **Integration speed:** Next (2–6w) • **Complexity:** Easy
**Explainer** — Imagine: A simple “Top Projects” watchlist you can act on in NOESIS and the Engine.
**Notes** — Parsed card in top AI implementations.txt

#### #38 — A) **Now (simple, high-ROI, low risk)**  _(General · Task · P2)_
**Status/Stage:** Inbox / Idea • **Owner:** ENERQIS • **RICE:** 9.8 (R=6.0, I=7.0, C=0.7, E=3.0)  
**When:** start  • due   • **Integration speed:** Next (2–6w) • **Complexity:** Easy
**Explainer** — Imagine: A) **Now (simple, high-ROI, low risk)** in NOESIS and the Engine.
**Tags** — `options,risk`
**Notes** — Parsed card in Stage 3 AI Driven.md

#### #39 — Acceptance gates (apply on ingest)  _(General · Task · P2)_
**Status/Stage:** Inbox / Idea • **Owner:** ENERQIS • **RICE:** 9.8 (R=6.0, I=7.0, C=0.7, E=3.0)  
**When:** start  • due   • **Integration speed:** Next (2–6w) • **Complexity:** Easy
**Explainer** — Imagine: Acceptance gates (apply on ingest) in NOESIS and the Engine.
**Tags** — `data,governance,spaceweather`
**Notes** — Parsed card in next level ideas.md

#### #40 — Acceptance gates (use on every data source)  _(General · Task · P2)_
**Status/Stage:** Inbox / Idea • **Owner:** ENERQIS • **RICE:** 9.8 (R=6.0, I=7.0, C=0.7, E=3.0)  
**When:** start  • due   • **Integration speed:** Next (2–6w) • **Complexity:** Easy
**Explainer** — Imagine: Acceptance gates (use on every data source) in NOESIS and the Engine.
**Tags** — `governance`
**Notes** — Parsed card in next level ideas.md

#### #41 — B) **Next (intermediate)**  _(General · Task · P2)_
**Status/Stage:** Inbox / Idea • **Owner:** ENERQIS • **RICE:** 9.8 (R=6.0, I=7.0, C=0.7, E=3.0)  
**When:** start  • due   • **Integration speed:** Next (2–6w) • **Complexity:** Easy
**Explainer** — Imagine: B) **Next (intermediate)** in NOESIS and the Engine.
**Notes** — Parsed card in Stage 3 AI Driven.md

#### #42 — Backlog seeds (paste to your CSV or use `add_backlog_item.ps1`)  _(General · Task · P2)_
**Status/Stage:** Inbox / Idea • **Owner:** ENERQIS • **RICE:** 9.8 (R=6.0, I=7.0, C=0.7, E=3.0)  
**When:** start  • due   • **Integration speed:** Next (2–6w) • **Complexity:** Easy
**Explainer** — Imagine: Backlog seeds (paste to your CSV or use `add_backlog_item.ps1`) in NOESIS and the Engine.
**Notes** — Parsed card in next level ideas.md

#### #43 — Backlog seeds (you can paste into your CSV later)  _(General · Task · P2)_
**Status/Stage:** Inbox / Idea • **Owner:** ENERQIS • **RICE:** 9.8 (R=6.0, I=7.0, C=0.7, E=3.0)  
**When:** start  • due   • **Integration speed:** Next (2–6w) • **Complexity:** Easy
**Explainer** — Imagine: Backlog seeds (you can paste into your CSV later) in NOESIS and the Engine.
**Notes** — Parsed card in next level ideas.md

#### #44 — C) **Advanced (Stage 3 halo)**  _(General · Task · P2)_
**Status/Stage:** Inbox / Idea • **Owner:** ENERQIS • **RICE:** 9.8 (R=6.0, I=7.0, C=0.7, E=3.0)  
**When:** start  • due   • **Integration speed:** Next (2–6w) • **Complexity:** Easy
**Explainer** — Imagine: C) **Advanced (Stage 3 halo)** in NOESIS and the Engine.
**Notes** — Parsed card in Stage 3 AI Driven.md

#### #45 — Canonical schemas (minute-level examples; UTC)  _(General · Task · P2)_
**Status/Stage:** Inbox / Idea • **Owner:** ENERQIS • **RICE:** 9.8 (R=6.0, I=7.0, C=0.7, E=3.0)  
**When:** start  • due   • **Integration speed:** Next (2–6w) • **Complexity:** Easy
**Explainer** — Imagine: Canonical schemas (minute-level examples; UTC) in NOESIS and the Engine.
**Notes** — Parsed card in next level ideas.md

#### #46 — Canonical schemas (parquet-ready)  _(General · Task · P2)_
**Status/Stage:** Inbox / Idea • **Owner:** ENERQIS • **RICE:** 9.8 (R=6.0, I=7.0, C=0.7, E=3.0)  
**When:** start  • due   • **Integration speed:** Next (2–6w) • **Complexity:** Easy
**Explainer** — Imagine: Canonical schemas (parquet-ready) in NOESIS and the Engine.
**Notes** — Parsed card in next level ideas.md

#### #47 — Core panes (v1 → v∞)  _(General · Task · P2)_
**Status/Stage:** Inbox / Idea • **Owner:** ENERQIS • **RICE:** 9.8 (R=6.0, I=7.0, C=0.7, E=3.0)  
**When:** start  • due   • **Integration speed:** Next (2–6w) • **Complexity:** Easy
**Explainer** — Imagine: Core panes (v1 → v∞) in NOESIS and the Engine.
**Notes** — Parsed card in Advanced coding paradigms + HUD.md

#### #48 — Evaluation discipline  _(General · Task · P2)_
**Status/Stage:** Inbox / Idea • **Owner:** ENERQIS • **RICE:** 9.8 (R=6.0, I=7.0, C=0.7, E=3.0)  
**When:** start  • due   • **Integration speed:** Next (2–6w) • **Complexity:** Easy
**Explainer** — Imagine: Evaluation discipline in NOESIS and the Engine.
**Notes** — Parsed card in next level ideas.md

#### #49 — Evaluation discipline (to avoid fake edge)  _(General · Task · P2)_
**Status/Stage:** Inbox / Idea • **Owner:** ENERQIS • **RICE:** 9.8 (R=6.0, I=7.0, C=0.7, E=3.0)  
**When:** start  • due   • **Integration speed:** Next (2–6w) • **Complexity:** Easy
**Explainer** — Imagine: Evaluation discipline (to avoid fake edge) in NOESIS and the Engine.
**Tags** — `options`
**Notes** — Parsed card in next level ideas.md

#### #50 — Evolution path  _(General · Task · P2)_
**Status/Stage:** Inbox / Idea • **Owner:** ENERQIS • **RICE:** 9.8 (R=6.0, I=7.0, C=0.7, E=3.0)  
**When:** start  • due   • **Integration speed:** Next (2–6w) • **Complexity:** Easy
**Explainer** — Imagine: Evolution path in NOESIS and the Engine.
**Notes** — Parsed card in Advanced coding paradigms + HUD.md

#### #51 — How it runs (Windows-first, grows with us)  _(General · Task · P2)_
**Status/Stage:** Inbox / Idea • **Owner:** ENERQIS • **RICE:** 9.8 (R=6.0, I=7.0, C=0.7, E=3.0)  
**When:** start  • due   • **Integration speed:** Next (2–6w) • **Complexity:** Easy
**Explainer** — Imagine: How it runs (Windows-first, grows with us) in NOESIS and the Engine.
**Notes** — Parsed card in Advanced coding paradigms + HUD.md

#### #52 — How we integrate this (quant discipline)  _(General · Task · P2)_
**Status/Stage:** Inbox / Idea • **Owner:** ENERQIS • **RICE:** 9.8 (R=6.0, I=7.0, C=0.7, E=3.0)  
**When:** start  • due   • **Integration speed:** Next (2–6w) • **Complexity:** Easy
**Explainer** — Imagine: How we integrate this (quant discipline) in NOESIS and the Engine.
**Notes** — Parsed card in next level ideas.md

#### #53 — If you want my literal “Top-10 leaderboard” (today)  _(General · Task · P2)_
**Status/Stage:** Inbox / Idea • **Owner:** ENERQIS • **RICE:** 9.8 (R=6.0, I=7.0, C=0.7, E=3.0)  
**When:** start  • due   • **Integration speed:** Next (2–6w) • **Complexity:** Easy
**Explainer** — Imagine: If you want my literal “Top-10 leaderboard” (today) in NOESIS and the Engine.
**Notes** — Parsed card in top AI implementations.txt

#### #54 — KPIs the HUD must move  _(General · Task · P2)_
**Status/Stage:** Inbox / Idea • **Owner:** ENERQIS • **RICE:** 9.8 (R=6.0, I=7.0, C=0.7, E=3.0)  
**When:** start  • due   • **Integration speed:** Next (2–6w) • **Complexity:** Easy
**Explainer** — Imagine: KPIs the HUD must move in NOESIS and the Engine.
**Tags** — `dashboard,spaceweather`
**Notes** — Parsed card in Advanced coding paradigms + HUD.md

#### #55 — M1) **Energy Manifold Mapper** (signature ENERQIS)  _(General · Task · P2)_
**Status/Stage:** Inbox / Idea • **Owner:** ENERQIS • **RICE:** 9.8 (R=6.0, I=7.0, C=0.7, E=3.0)  
**When:** start  • due   • **Integration speed:** Next (2–6w) • **Complexity:** Easy
**Explainer** — Imagine: M1) **Energy Manifold Mapper** (signature ENERQIS) in NOESIS and the Engine.
**Tags** — `manifold,spaceweather`
**Notes** — Parsed card in top AI implementations.txt

#### #56 — M2) **Causal Markets Engine**  _(General · Task · P2)_
**Status/Stage:** Inbox / Idea • **Owner:** ENERQIS • **RICE:** 9.8 (R=6.0, I=7.0, C=0.7, E=3.0)  
**When:** start  • due   • **Integration speed:** Next (2–6w) • **Complexity:** Easy
**Explainer** — Imagine: M2) **Causal Markets Engine** in NOESIS and the Engine.
**Tags** — `causal`
**Notes** — Parsed card in top AI implementations.txt

#### #57 — M3) **Meta-Alpha Compiler**  _(General · Task · P2)_
**Status/Stage:** Inbox / Idea • **Owner:** ENERQIS • **RICE:** 9.8 (R=6.0, I=7.0, C=0.7, E=3.0)  
**When:** start  • due   • **Integration speed:** Next (2–6w) • **Complexity:** Easy
**Explainer** — Imagine: M3) **Meta-Alpha Compiler** in NOESIS and the Engine.
**Notes** — Parsed card in top AI implementations.txt

#### #58 — M4) **Differentiable Backtester**  _(General · Task · P2)_
**Status/Stage:** Inbox / Idea • **Owner:** ENERQIS • **RICE:** 9.8 (R=6.0, I=7.0, C=0.7, E=3.0)  
**When:** start  • due   • **Integration speed:** Next (2–6w) • **Complexity:** Hard
**Explainer** — Imagine: M4) **Differentiable Backtester** in NOESIS and the Engine.
**Notes** — Parsed card in top AI implementations.txt

#### #59 — M5) **Ethical Impact Loop**  _(General · Task · P2)_
**Status/Stage:** Inbox / Idea • **Owner:** ENERQIS • **RICE:** 9.8 (R=6.0, I=7.0, C=0.7, E=3.0)  
**When:** start  • due   • **Integration speed:** Next (2–6w) • **Complexity:** Easy
**Explainer** — Imagine: M5) **Ethical Impact Loop** in NOESIS and the Engine.
**Tags** — `execution`
**Notes** — Parsed card in top AI implementations.txt

#### #60 — NOESIS — What it is  _(General · Task · P2)_
**Status/Stage:** Inbox / Idea • **Owner:** ENERQIS • **RICE:** 9.8 (R=6.0, I=7.0, C=0.7, E=3.0)  
**When:** start  • due   • **Integration speed:** Next (2–6w) • **Complexity:** Easy
**Explainer** — Imagine: NOESIS — What it is in NOESIS and the Engine.
**Tags** — `dashboard`
**Notes** — Parsed card in Advanced coding paradigms + HUD.md

#### #61 — Pilot set (fastest to add with real edge potential)  _(General · Task · P2)_
**Status/Stage:** Inbox / Idea • **Owner:** ENERQIS • **RICE:** 9.8 (R=6.0, I=7.0, C=0.7, E=3.0)  
**When:** start  • due   • **Integration speed:** Next (2–6w) • **Complexity:** Easy
**Explainer** — Imagine: Pilot set (fastest to add with real edge potential) in NOESIS and the Engine.
**Notes** — Parsed card in next level ideas.md

#### #62 — Practical cautions  _(General · Task · P2)_
**Status/Stage:** Inbox / Idea • **Owner:** ENERQIS • **RICE:** 9.8 (R=6.0, I=7.0, C=0.7, E=3.0)  
**When:** start  • due   • **Integration speed:** Next (2–6w) • **Complexity:** Easy
**Explainer** — Imagine: Practical cautions in NOESIS and the Engine.
**Notes** — Parsed card in next level ideas.md

#### #63 — Practical cautions (edge preservation)  _(General · Task · P2)_
**Status/Stage:** Inbox / Idea • **Owner:** ENERQIS • **RICE:** 9.8 (R=6.0, I=7.0, C=0.7, E=3.0)  
**When:** start  • due   • **Integration speed:** Next (2–6w) • **Complexity:** Easy
**Explainer** — Imagine: Practical cautions (edge preservation) in NOESIS and the Engine.
**Notes** — Parsed card in next level ideas.md

#### #64 — Prioritized “start now” set (highest ROI)  _(General · Task · P2)_
**Status/Stage:** Inbox / Idea • **Owner:** ENERQIS • **RICE:** 9.8 (R=6.0, I=7.0, C=0.7, E=3.0)  
**When:** start  • due   • **Integration speed:** Next (2–6w) • **Complexity:** Easy
**Explainer** — Imagine: Prioritized “start now” set (highest ROI) in NOESIS and the Engine.
**Tags** — `options`
**Notes** — Parsed card in next level ideas.md

#### #65 — TL;DR (what to do now)  _(General · Task · P2)_
**Status/Stage:** Inbox / Idea • **Owner:** ENERQIS • **RICE:** 9.8 (R=6.0, I=7.0, C=0.7, E=3.0)  
**When:** start  • due   • **Integration speed:** Next (2–6w) • **Complexity:** Easy
**Explainer** — Imagine: TL;DR (what to do now) in NOESIS and the Engine.
**Notes** — Parsed card in top AI implementations.txt

#### #66 — What this means for ENERQIS (quick synthesis)  _(General · Task · P2)_
**Status/Stage:** Inbox / Idea • **Owner:** ENERQIS • **RICE:** 9.8 (R=6.0, I=7.0, C=0.7, E=3.0)  
**When:** start  • due   • **Integration speed:** Next (2–6w) • **Complexity:** Easy
**Explainer** — Imagine: What this means for ENERQIS (quick synthesis) in NOESIS and the Engine.
**Tags** — `dashboard`
**Notes** — Parsed card in top AI implementations.txt

#### #67 — What to do next (no-drama checklist)  _(General · Task · P2)_
**Status/Stage:** Inbox / Idea • **Owner:** ENERQIS • **RICE:** 9.8 (R=6.0, I=7.0, C=0.7, E=3.0)  
**When:** start  • due   • **Integration speed:** Next (2–6w) • **Complexity:** Easy
**Explainer** — Imagine: What to do next (no-drama checklist) in NOESIS and the Engine.
**Notes** — Parsed card in Stage 3 AI Driven.md

#### #68 — What we do next (tactical)  _(General · Task · P2)_
**Status/Stage:** Inbox / Idea • **Owner:** ENERQIS • **RICE:** 9.8 (R=6.0, I=7.0, C=0.7, E=3.0)  
**When:** start  • due   • **Integration speed:** Next (2–6w) • **Complexity:** Easy
**Explainer** — Imagine: What we do next (tactical) in NOESIS and the Engine.
**Notes** — Parsed card in top AI implementations.txt

#### #69 — Why it matters  _(General · Task · P2)_
**Status/Stage:** Inbox / Idea • **Owner:** ENERQIS • **RICE:** 9.8 (R=6.0, I=7.0, C=0.7, E=3.0)  
**When:** start  • due   • **Integration speed:** Next (2–6w) • **Complexity:** Easy
**Explainer** — Imagine: Why it matters in NOESIS and the Engine.
**Notes** — Parsed card in Advanced coding paradigms + HUD.md

CAPTURE: [Security]|Task|P0|Adopt sops/age secrets with .sops.yaml; encrypt .env.enc; rotate any exposed tokens
CAPTURE: [CI]|Task|P0|Pin GitHub Actions by commit SHA; enable CodeQL + Dependabot (security+versions)
CAPTURE: [Execution]|Task|P0|Implement shared risk module (kill-switch, daily loss cap, position caps) and wire into all cBots
CAPTURE: [Integrity]|Task|P0|Minisign config signing; verify at runtime (block on invalid signature)
CAPTURE: [IIS]|Task|P0|Enable OCR (Tesseract+pytesseract); set G-IIS-OCR-REQUIRED to error
CAPTURE: [Policy]|Task|P0|Add LLM usage policy (no proprietary code to public endpoints; redaction; local-only for sensitive)
CAPTURE: [EREP]|Task|P1|Add code gates (build/style/risk/backtest) and overlays CODE:build:v1
CAPTURE: [Data]|Task|P1|Emit SBOM (CycloneDX) + hash manifest on snapshots; gate G-ARTIFACT-HASH
CAPTURE: [NOESIS]|Task|P1|Add alerts: loss_cap_trip, slippage_3σ, gate_fail; wire execution mark-out telemetry
CAPTURE: [Legal]|Task|P1|Add NDA + IP Assignment templates; start ENERQIS/NOESIS trademark search
