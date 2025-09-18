Param([int]$MaxMissionControlAgeDays = 7)

$ErrorActionPreference = "Stop"
$errors = @()

# 1) Uncommitted changes (must be clean before packaging)
$gitStatus = git status --porcelain
if ($gitStatus) { $errors += "Uncommitted changes in working tree." }

# 2) Mission Control freshness
$mc = "13_OpsLog\mission_control.md"
if (Test-Path $mc) {
  $ageDays = (New-TimeSpan -Start (Get-Item $mc).LastWriteTimeUtc -End (Get-Date).ToUniversalTime()).Duration().TotalDays
  if ($ageDays -gt $MaxMissionControlAgeDays) { $errors += "Mission Control older than $MaxMissionControlAgeDays days." }
} else { $errors += "Mission Control missing: 13_OpsLog/mission_control.md" }

# 3) Backlog & Scorecard presence
$backlogCsv = "13_OpsLog\TODO\enerqis_backlog.csv"
$scoreCsv   = "13_OpsLog\ROADMAP\LIVING_SCORECARD\living_scorecard.csv"
if (-not (Test-Path $backlogCsv)) { $errors += "Backlog CSV missing: $backlogCsv" }
if (-not (Test-Path $scoreCsv))   { $errors += "Living Scorecard CSV missing: $scoreCsv" }

# 4) Pending editorial patchsets (optional: require PR workflow before package)
$patchDir = "13_OpsLog\CHANGES\patches"
if (Test-Path $patchDir) {
  $pending = Get-ChildItem $patchDir -Recurse -Filter *.patch -ErrorAction SilentlyContinue
  if ($pending.Count -gt 0) { $errors += "Editorial patchsets pending review: $($pending.Count)" }
}

# Emit report
$report = "00_repo\.cbr\reports\ops_debt_report.json"
$null = New-Item -ItemType Directory -Force -Path (Split-Path $report)
if ($errors.Count -gt 0) {
  [pscustomobject]@{
    timestamp = (Get-Date).ToString("o")
    status    = "fail"
    errors    = $errors
  } | ConvertTo-Json -Depth 5 | Set-Content -Encoding utf8 $report
  $errors | ForEach-Object { Write-Host " - $_" }
  exit 1
} else {
  [pscustomobject]@{
    timestamp = (Get-Date).ToString("o")
    status    = "green"
    checks    = @("clean tree","mission_control fresh","backlog+scorecard present","no pending patches")
  } | ConvertTo-Json -Depth 5 | Set-Content -Encoding utf8 $report
  Write-Host "Ops debt: none"
  exit 0
}
