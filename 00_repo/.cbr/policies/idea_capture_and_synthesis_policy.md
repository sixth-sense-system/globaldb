# Idea Capture & Synthesis Policy (IIS) — v1.0
Date: 2025-09-15
Owner: ENERQIS Ops
Status: Active
Applies to: Human-sourced ideas/concepts, prioritized sets (“Start now”, “Pilot”), and agent-surfaced unlocks.

## Purpose
Make human knowledge a first‑class ingestion stream, governed like any dataset: normalized, deduped, ranked, auditable, and synchronized with Roadmap/Scorecard/NOESIS.

## Scope & Definitions
- **IIS**: Idea Capture & Synthesis — this policy.
- **H‑Tier (Human)**: Ingestion tier for ideas from chats, notes, RFCs, research summaries (not raw market data).
- **Canonical Backlog**: `13_OpsLog/TODO/enerqis_backlog.csv` (+ card view: `13_OpsLog/ROADMAP/enerqis_backlog.md`).
- **Scorecard**: `13_OpsLog/ROADMAP/LIVING_SCORECARD/*` (execution slice & KPIs).
- **Pass**: One merge/dedupe/rank cycle across all sources at a point in time.

## Triggers
- New zip or text dump of ideas (chat excerpts, CAPTURE lines, cards).
- Weekly cadence or on‑demand before planning.
- EREP Discovery/Synthesis completion events.

## Inputs (accepted formats)
- CSV/MD backlog files (current canonical pair).
- `.md` / `.txt` idea dumps:  
  - **CAPTURE line**: `[Theme]|Type|Priority|Title — one-line description`  
  - **Card**:
    ```
    ### Title
    Theme: …
    Type: Idea|Task|RFC
    Priority: P0|P1|P2|P3
    What: …
    Why: …
    How: …
    Test: …
    Charts: …
    Correlations: …
    Links: …
    Dependencies: …
    Benefits: …
    ```

## Normalization
- Map to v2 schema (superset): identity/planning, RICE fields, semantics (What/Why/How/…),
  plus **Explainer**, **Integration speed**, **Complexity**, **Tags**, **Provenance**.
- Auto‑tag from keywords/domains (e.g., `orderflow, execution, spaceweather, gann, agentic, ctrader`).

## Dedupe & Merge
- Key = `slug(Theme) + ":" + slug(Title)` + fuzzy title similarity ≥ 0.82 (same theme).
- Merge rule: prefer non‑empty; keep richer text; union `links/tags/related_ids`;
  **lowest priority wins** (P0>P1>P2>P3); keep most advanced `stage`.

## Ranking (Stage‑1 weighted, revenue‑first)
```
RICE+ = (R*I*C/E) × Stage1RevenueWeight × VelocityWeight / ComplexityPenalty
```
- **Stage1RevenueWeight**: direct path to **live cBots on FxPro cTrader (WTI/SPX)** = 1.35; enabling infra = 1.20; research = 1.00.
- **VelocityWeight**: Now/Pilot = 1.15; Next = 1.00; Later = 0.90.
- **ComplexityPenalty**: Easy 1.0; Medium 1.1; Hard 1.3.

## Status Transitions
- Never delete; move Done to `status=Done`.
- New accepted “Start now” → `status=InProgress`, `timeframe=Now`.
- Blocked items require `notes` reason.

## Outputs (each Pass)
1. **Backlog CSV** — `13_OpsLog/TODO/enerqis_backlog.csv` (canonical, re‑ranked).  
2. **Backlog MD** — `13_OpsLog/ROADMAP/enerqis_backlog.md` (cards grouped by Timeframe→Priority).  
3. **OpsLog entry** — “RUN: Discovery/Synthesis — Backlog refresh (YYYY‑MM‑DD)” with Top‑N Now set + rationale.  
4. **Blueprint sync** — update `05_Blueprint/roadmap_blueprint.md` (capabilities) and `05_Blueprint/development_roadmap.md` (milestones) referencing item IDs.  
5. **Scorecard sync** — push owners/dates/status to `LIVING_SCORECARD/*` and reflect changes back to backlog shared fields.

## Governance & Gates (see acceptance_gates_idea.yaml)
- G‑IDEA‑CAPTURE‑FORMAT: inputs conform to CAPTURE/Card/CSV.  
- G‑IDEA‑DEDUPED: duplicates merged; provenance kept.  
- G‑IDEA‑RANKED‑STAGE1: RICE+ applied with current weights.  
- G‑IDEA‑OPSLOG: Ops entry posted with Top‑N Now set & links.  
- G‑IDEA‑BLUEPRINT‑SYNC: Blueprint updated to reflect accepted set.  
- G‑IDEA‑SCORECARD‑SYNC: Scorecard reflects owners, KPIs, milestones.

## NOESIS
- Display “Now” lane and Top‑N with **Explainer**, **Benefits**, **ETA**, **Complexity**; one‑click open PR/spec.  
- Snapshot writer drops tiles into `13_OpsLog/SNAPSHOTS/` for audit.

## Versioning
- This policy is versioned under `00_repo/.cbr/policies/` and referenced by `erep_policy.json` policy set `IIS:v1.0`.
