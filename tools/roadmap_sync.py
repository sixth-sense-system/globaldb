import argparse, pathlib, csv, datetime


def read_backlog(p):
    if not pathlib.Path(p).exists():
        return []
    with open(p, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_scorecard(csv_path, md_path, now, nxt, later):
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["bucket", "id", "title", "theme", "priority", "owner", "eta"])
        for b, arr in [("Now", now), ("Next", nxt), ("Later", later)]:
            for it in arr:
                w.writerow(
                    [
                        b,
                        it.get("id", ""),
                        it.get("title", ""),
                        it.get("theme", ""),
                        it.get("priority", ""),
                        "ENERQIS",
                        "TBD",
                    ]
                )
    lines = ["# Living Scorecard — " + datetime.date.today().isoformat(), ""]
    for name, arr in [("Now", now), ("Next", nxt), ("Later", later)]:
        lines.append("## " + name)
        for it in arr:
            lines.append(
                f"- **{it.get('title','')}** — [{it.get('theme','')}] {it.get('priority','')} (id:{it.get('id','')})"
            )
        lines.append("")
    pathlib.Path(md_path).write_text("\n".join(lines), encoding="utf-8")


def write_mission(path, now):
    lines = [
        "# Mission Control — " + datetime.date.today().isoformat(),
        "",
        "This is your daily home base.",
        "## NOW (do in order)",
    ]
    for i, it in enumerate(now, 1):
        lines += [
            f"{i}. **{it.get('title','')}**  _[{it.get('theme','')}] {it.get('priority','')}_",
            "   - Why: (fill from backlog)",
            "   - How: (link to runbook / steps)",
            "   - Done: gates/tests green",
        ]
    pathlib.Path(path).write_text("\n".join(lines), encoding="utf-8")


def update_dev_roadmap(p):
    P = pathlib.Path(p)
    base = P.read_text(encoding="utf-8") if P.exists() else "# Development Roadmap\n"
    base += (
        "\n\n## Sync "
        + datetime.date.today().isoformat()
        + "\n- Synced from latest Discovery/Synthesis pass.\n"
    )
    P.write_text(base, encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--backlogCsv", required=True)
    ap.add_argument("--backlogMd", required=True)
    ap.add_argument("--scoreCsv", required=True)
    ap.add_argument("--scoreMd", required=True)
    ap.add_argument("--devRoadmap", required=True)
    ap.add_argument("--mission", required=True)
    a = ap.parse_args()

    items = read_backlog(a.backlogCsv)
    now = [it for it in items if (it.get("priority", "") or "").upper() == "P0"][:12]
    nxt = [it for it in items if (it.get("priority", "") or "").upper() == "P1"][:20]
    later = [
        it for it in items if (it.get("priority", "") or "").upper() not in ("P0", "P1")
    ]

    write_scorecard(a.scoreCsv, a.scoreMd, now, nxt, later)
    write_mission(a.mission, now)
    update_dev_roadmap(a.devRoadmap)
    print(
        "Roadmap Sync wrote living_scorecard.*, mission_control.md, and updated development_roadmap.md."
    )


if __name__ == "__main__":
    main()
