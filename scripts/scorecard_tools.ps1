param(
  [string]$ScorecardCsv = "13_OpsLog\ROADMAP\living_scorecard.csv",
  [string]$SnapshotDir  = "13_OpsLog\ROADMAP\snapshots"
)
if (!(Test-Path $ScorecardCsv)) { Write-Error "Missing $ScorecardCsv"; exit 1 }
$ts = Get-Date -Format "yyyyMMdd-HHmm"
New-Item -ItemType Directory -Force -Path $SnapshotDir | Out-Null
Copy-Item $ScorecardCsv "$SnapshotDir\living_scorecard_$ts.csv"
"Snapshot saved to $SnapshotDir\living_scorecard_$ts.csv"
