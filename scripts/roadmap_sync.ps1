param(
  [string]$BacklogCsv = ".\enerqis_backlog.csv",
  [string]$BacklogMd = ".\enerqis_backlog.md",
  [string]$ScoreCsv = ".\13_OpsLog\ROADMAP\LIVING_SCORECARD\living_scorecard.csv",
  [string]$ScoreMd = ".\13_OpsLog\ROADMAP\LIVING_SCORECARD\living_scorecard.md",
  [string]$DevRoadmap = ".\05_Blueprint\development_roadmap.md",
  [string]$Mission = ".\13_OpsLog\ROADMAP\MASTER\mission_control.md"
)
$py = ".\tools\roadmap_sync.py"
if (!(Test-Path $py)) { throw "Sync tool not found: $py" }
python $py --backlogCsv "$BacklogCsv" --backlogMd "$BacklogMd" `
  --scoreCsv "$ScoreCsv" --scoreMd "$ScoreMd" --devRoadmap "$DevRoadmap" --mission "$Mission"
Write-Host "Roadmap Sync complete."
