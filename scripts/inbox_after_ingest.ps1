Param(
  [string]$InboxRoot = "11_Research\INBOX",
  [string]$ProcessedRoot = "11_Research\PROCESSED",
  [string]$ExtractedJsonl = "00_repo\.cbr\out\extracted.jsonl",
  [string]$UrlsCsv = "11_Research\INBOX\urls.csv",
  [switch]$DryRun = $false
)

$ErrorActionPreference = "Stop"

function Read-Jsonl($path) {
  if (-not (Test-Path $path)) { return @() }
  $lines = Get-Content -Raw -Encoding UTF8 $path -ErrorAction Stop -TotalCount 100000
  if (-not $lines) { return @() }
  return ($lines -split "`n" | Where-Object { $_.Trim() -ne "" } | ForEach-Object { $_ | ConvertFrom-Json })
}

function Load-Csv($path) {
  if (-not (Test-Path $path)) { return @() }
  return Import-Csv -Path $path
}

function Save-Csv($rows, $path) {
  $dir = Split-Path $path
  if ($dir) { New-Item -ItemType Directory -Force -Path $dir | Out-Null }
  $rows | Export-Csv -Path $path -NoTypeInformation -Encoding UTF8
}

$today = Get-Date -Format "yyyyMMdd"
$processedDir = Join-Path $ProcessedRoot $today
New-Item -ItemType Directory -Force -Path $processedDir | Out-Null
New-Item -ItemType Directory -Force -Path "13_OpsLog\machine" | Out-Null

# 1) Parse extracted.jsonl → collect local paths + URLs
$records = Read-Jsonl $ExtractedJsonl
$localPaths = @()
$urlsSeen = @()

foreach ($r in $records) {
  $sp = $r.source.path
  $su = $r.source.url
  if ($sp -and ($sp -match [regex]::Escape($InboxRoot))) {
    # Normalize to Windows path separators
    $np = $sp -replace '/', '\'
    $localPaths += (Resolve-Path -LiteralPath $np -ErrorAction SilentlyContinue)
  }
  if ($su) { $urlsSeen += $su }
}

$localPaths = $localPaths | Sort-Object -Unique
$urlsSeen = $urlsSeen | Sort-Object -Unique

# 2) Move matched local files to PROCESSED/<date>
$moves = @()
foreach ($p in $localPaths) {
  if (-not $p) { continue }
  $src = $p.Path
  $rel = Resolve-Path $src -Relative
  # Preserve subfolder structure below INBOX
  $relSub = $rel -replace [regex]::Escape($InboxRoot), ""
  $relSub = $relSub.TrimStart('\')
  $dest = Join-Path $processedDir $relSub
  $destDir = Split-Path $dest
  if ($DryRun) {
    $moves += [pscustomobject]@{ action="move"; from=$rel; to=(Resolve-Path $destDir -ErrorAction SilentlyContinue); file=[IO.Path]::GetFileName($dest) }
  } else {
    New-Item -ItemType Directory -Force -Path $destDir | Out-Null
    Move-Item -Force -LiteralPath $src -Destination $dest
    $moves += [pscustomobject]@{ action="moved"; from=$rel; to=(Resolve-Path $destDir -ErrorAction SilentlyContinue); file=[IO.Path]::GetFileName($dest) }
  }
}

# 3) Update urls.csv with status=processed for seen URLs
$urlsCsvRows = @()
if (Test-Path $UrlsCsv) {
  $urlsCsvRows = Load-Csv $UrlsCsv
  $ts = (Get-Date).ToString("o")
  foreach ($row in $urlsCsvRows) {
    if ($urlsSeen -contains $row.url) {
      $row.status = "processed"
      $row.processed_at = $ts
    }
  }
  if (-not $DryRun) {
    Save-Csv $urlsCsvRows $UrlsCsv
  }
}

# 4) Emit audit log
$log = [pscustomobject]@{
  timestamp = (Get-Date).ToString("o")
  dry_run   = [bool]$DryRun
  moved     = $moves
  urls_seen = $urlsSeen
}
$logPath = "13_OpsLog\machine\inbox_moves.log.json"
$log | ConvertTo-Json -Depth 6 | Set-Content -Encoding utf8 $logPath

Write-Host "INBOX Flow complete. Moved $($moves.Count) files. URLs processed: $($urlsSeen.Count)."
if ($DryRun) { Write-Host "(dry-run: no changes made)" }
