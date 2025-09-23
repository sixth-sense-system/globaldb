import os, datetime as dt
from pathlib import Path
import pandas as pd, pyarrow.parquet as pq

ROOT = Path(".")
DATA = ROOT / "13_OpsLog" / "data"
VIEWS = ROOT / "13_OpsLog" / "views"
MC = ROOT / "05_Blueprint" / "MASTER"
VIEWS.mkdir(parents=True, exist_ok=True)
MC.mkdir(parents=True, exist_ok=True)


def now_utc_iso():
    return dt.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"


def read_parquet(name):
    p = DATA / f"{name}.parquet"
    return pq.read_table(p).to_pandas() if p.exists() else pd.DataFrame()


def write_text(path: Path, text: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.strip() + "\n", encoding="utf-8")


def render_history(events: pd.DataFrame) -> str:
    if events.empty:
        return "# Living History\n> First run will populate after ingest.\n"
    ev = events.copy().sort_values("date")
    lines = [
        "# ENERQIS / NOESIS — Living History",
        "",
    ]
    current_month = None
    for _, r in ev.iterrows():
        m = str(r["date"])[:7]
        if m != current_month:
            lines.append(f"## {m}")
            current_month = m
        lines.append(f"- **{r['id']}** — {r['title']} ({r['date']})")
    lines.append(f"\n*Generated {now_utc_iso()}*")
    return "\n".join(lines)


def render_decisions(decisions: pd.DataFrame) -> str:
    if decisions.empty:
        return "# Decisions (ADR Index)\n> First run will populate after ingest.\n"
    de = decisions.copy().sort_values(["date", "id"])
    lines = ["# Decisions (ADR Index)", ""]
    for _, r in de.iterrows():
        lines.append(f"- **{r['id']}** ({r['status']}) — {r['date']}")
    lines.append(f"\n*Generated {now_utc_iso()}*")
    return "\n".join(lines)


def render_systems(configs: pd.DataFrame) -> str:
    if configs.empty:
        return "# Systems — Enforced Rules & Why\n> First run will populate after ingest.\n"
    cf = configs.copy().sort_values(["area", "version"])
    lines = ["# Systems — Enforced Rules & Why", ""]
    for _, r in cf.iterrows():
        lines.append(f"- **{r['id']}** [{r['status']}] — {r['area']} (v{r['version']})")
    lines.append(f"\n*Generated {now_utc_iso()}*")
    return "\n".join(lines)


def render_exec_scorecard(scorecard: pd.DataFrame) -> str:
    if scorecard.empty:
        return "# Executive Scorecard\n> First run will populate after ingest.\n"
    sc = scorecard.copy()
    # numbering: last pulse week becomes this scorecard #
    pulses = sc[sc["record_type"] == "pulse"].sort_values("week_start")
    sc_num = len(pulses)
    date_range = ""
    if not pulses.empty:
        start = str(pulses["week_start"].iloc[-1])
        # best effort: show last 7-day span; real span can be added by the consolidator
        date_range = f" (Week starting {start})"
    lines = [f"# Executive Scorecard #{sc_num}{date_range}", ""]
    # Metrics table (v2)
    m = sc[sc["record_type"] == "metric"]
    if not m.empty:
        lines.append("| Metric | Now | 6–12 mo | 2–3 yr | What a 10 is |")
        lines.append("|---|---:|---:|---:|---|")
        for _, r in m.iterrows():
            lines.append(
                f"| {r.get('label','')} | {r.get('now','')} | {r.get('h6_12mo','')} | {r.get('ceiling_2_3y','')} | {r.get('definition_of_10_md','').replace('|','\\|')} |"
            )
        lines.append("")
    # Why scores rose / Levers
    why = m[~m["rationale_md"].isna()]
    if not why.empty:
        lines.append("## Why the scores rose\n")
        for _, r in why.iterrows():
            lines.append(f"**{r['label']}** — {r['rationale_md']}")
        lines.append("")
    lev = m[~m["levers_md"].isna()]
    if not lev.empty:
        lines.append("## Levers to reach 9.5–10\n")
        for _, r in lev.iterrows():
            lines.append(f"**{r['label']}** — {r['levers_md']}")
        lines.append("")
    # Financial tiers
    ft = sc[sc["record_type"] == "financial_tier"]
    if not ft.empty:
        lines.append("## Financial outcome probabilities (12–24m)\n")
        for _, r in ft.iterrows():
            lines.append(
                f"- **${r['tier']}** — **{r['prob_today']}%**  \n  {r.get('assumptions_md','')}"
            )
        lines.append("")
    # Valuation snapshot
    val = sc[sc["record_type"] == "valuation"]
    if not val.empty:
        lines.append("## Executive Valuation Snapshot\n")
        for _, r in val.iterrows():
            lines.append(
                f"- **{r['org_type']}** {r.get('timeframe','')}: **${r.get('replace_cost_low','?')}–${r.get('replace_cost_high','?')}**  \n  {r.get('scope_md','')}"
            )
        lines.append("")
    # Pulse (this week)
    if not pulses.empty:
        r = pulses.iloc[-1]
        lines.append("## Executive Pulse (this week)\n")
        lines.append(f"**Headlines**\n\n{r.get('headlines_md','')}\n")
        lines.append(f"**What shipped**\n\n{r.get('what_shipped_md','')}\n")
        lines.append(
            f"**Perceived value delta:** ${r.get('value_delta_low','?')}–${r.get('value_delta_high','?')}\n"
        )
        if pd.notna(r.get("open_risks_md", None)):
            lines.append(f"**Open risks**\n\n{r.get('open_risks_md','')}\n")
        if pd.notna(r.get("roi_notes_md", None)):
            lines.append(f"**ROI notes**\n\n{r.get('roi_notes_md','')}\n")
        lines.append("")
    lines.append(f"*Generated {now_utc_iso()}*")
    return "\n".join(lines)


def render_next(roadmap: pd.DataFrame) -> str:
    # Select near-term scheduled items
    if roadmap.empty:
        return "# NEXT — The 7–12 Moves For The Week\n\n> Populates after triage.\n"
    rm = roadmap.copy()
    rm = (
        rm[rm["status"].isin(["planned", "scheduled", "in_progress"])]
        .sort_values(["stage", "window", "id"])
        .head(12)
    )
    lines = ["# NEXT — The 7–12 Moves For The Week", ""]
    for _, r in rm.iterrows():
        deps = (
            ", ".join(r["depends_on"]) if isinstance(r.get("depends_on"), list) else "-"
        )
        lines.append(
            f"- [ ] **{r['title']}** — Owner: {r.get('owner','you')} — Evidence: {', '.join(r.get('evidence_targets',[])) if isinstance(r.get('evidence_targets'), list) else '-'} — Depends: {deps}"
        )
    lines.append(f"\n*Generated {now_utc_iso()}*")
    return "\n".join(lines)


def render_roapmap(roadmap: pd.DataFrame) -> str:
    if roadmap.empty:
        return (
            "# Roadmap — Execution Schedule\n> First run will populate after ingest.\n"
        )
    rm = roadmap.copy().sort_values(["stage", "window", "id"])
    lines = ["# Roadmap — Execution Schedule", ""]
    lines.append("| Stage | Window | ID | Title | Status |")
    lines.append("|---|---|---|---|---|")
    for _, r in rm.iterrows():
        lines.append(
            f"| {r['stage']} | {r['window']} | {r['id']} | {r['title']} | {r['status']} |"
        )
    lines.append(f"\n*Generated {now_utc_iso()}*")
    return "\n".join(lines)


def render_mission_control(next_md: str, scorecard: pd.DataFrame) -> str:
    # Simple KPI header from latest metrics + linkouts
    lines = ["# Mission Control — This Week", ""]
    # KPI snapshot
    m = scorecard[scorecard["record_type"] == "metric"]
    if not m.empty:
        # pick 5–7 core KPIs to show (governance, infra, data, systems, ai)
        top = m[
            m["domain"].isin(
                [
                    "Governance/Determinism",
                    "Infrastructure & Security",
                    "Data Layer",
                    "Systems",
                    "AI/Algo",
                ]
            )
        ].copy()
        if top.empty:
            top = m.copy()
        top = top.sort_values("label").head(7)
        lines.append("## KPI Snapshot\n")
        lines.append("| KPI | Now | 6–12 mo |")
        lines.append("|---|---:|---:|")
        for _, r in top.iterrows():
            lines.append(
                f"| {r['label']} | {r.get('now','')} | {r.get('h6_12mo','')} |"
            )
        lines.append("")
    # Short links
    lines.append(
        "**Quick Links:** [History](../../13_OpsLog/views/HISTORY.md) • [Roadmap](../../13_OpsLog/views/ROADMAP.md) • [Scorecard](../../13_OpsLog/views/EXEC_SCORECARD.md)"
    )
    lines.append("\n---\n")
    lines.append(next_md.strip())
    lines.append(f"\n*Generated {now_utc_iso()}*")
    return "\n".join(lines)


def main():
    events = read_parquet("events")
    decisions = read_parquet("decisions")
    configs = read_parquet("configs")
    ideas = read_parquet("ideas")
    roadmap = read_parquet("roadmap")
    scorecard = read_parquet("scorecard")

    write_text(VIEWS / "HISTORY.md", render_history(events))
    write_text(VIEWS / "DECISIONS.md", render_decisions(decisions))
    write_text(VIEWS / "SYSTEMS.md", render_systems(configs))
    write_text(VIEWS / "EXEC_SCORECARD.md", render_exec_scorecard(scorecard))
    next_md = render_next(roadmap)
    write_text(VIEWS / "NEXT.md", next_md)
    write_text(VIEWS / "ROADMAP.md", render_roapmap(roadmap))
    # Mission Control mirror
    write_text(MC / "mission_control.md", render_mission_control(next_md, scorecard))


if __name__ == "__main__":
    main()
