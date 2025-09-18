Param(
  [Parameter(Mandatory=$true)][string]$Input
)

$ErrorActionPreference = "Stop"

function Read-AllText($p) { Get-Content -Path $p -Raw -Encoding UTF8 }

function Normalize-Title($t) {
  $t = $t.Trim()
  $t = $t -replace "^[#\s\-–•\d\.\)]*\s*", ""
  $t = $t -replace "\s+", " "
  return $t
}

function StageRank($title) {
  $t = $title.ToLower()
  if ($t -match "git|branch|commit|push|ssh|gpg|github") { return 10 }
  if ($t -match "governance|policy|gate|overlay|acceptance") { return 20 }
  if ($t -match "erep|hooks|full package|compliance|manifest|snapshot") { return 30 }
  if ($t -match "iis|discovery|erip|ingest") { return 40 }
  if ($t -match "synthesis|editorial|mechanical") { return 50 }
  if ($t -match "inbox|urls.csv|extracted.jsonl") { return 60 }
  if ($t -match "mission control|runbook|scorecard|progress") { return 70 }
  if ($t -match "package|ship|seal") { return 80 }
  if ($t -match "strategy|cbot|backtest|factory") { return 90 }
  return 55
}

function Extract-Steps($text) {
  $lines = $text -split "`n"
  $blocks = @()
  $current = $null
  $inFence = $false

  for ($i=0; $i -lt $lines.Count; $i++) {
    $line = $lines[$i]

    if ($line -match "^\s*```") {
      $inFence = -not $inFence
      continue
    }
    if ($inFence) { continue }

    if ($line -match "^(###|##)\s+(.*)$" -or $line -match "^\s*STEP:\s*(.+)$") {
      if ($current) { $blocks += $current }
      $title = $line -replace "^(###|##)\s+", ""
      $title = $title -replace "^\s*STEP:\s*", ""
      $current = [ordered]@{ title = (Normalize-Title $title); body = @(); start = $i }
    } elseif ($current) {
      $current.body += $line
    }
  }
  if ($current) { $blocks += $current }

  if ($blocks.Count -eq 0) {
    $paras = -split $text, "\r?\n\r?\n"
    $idx = 1
    foreach ($p in $paras) {
      $t = $p.Trim()
      if ($t -eq "") { continue }
      $title = $t.Split("`n")[0]
      if ($title.Length -gt 80) { $title = $title.Substring(0,80) + "…" }
      $blocks += [ordered]@{ title = (Normalize-Title $title); body = ($t -split "`n"); start = $idx }
      $idx++
    }
  }
  return $blocks
}

function Merge-Dups($blocks) {
  $map = @{}
  foreach ($b in $blocks) {
    $key = (Normalize-Title $b.title).ToLower()
    if ($map.ContainsKey($key)) {
      $prev = $map[$key]
      $merged = New-Object System.Collections.Generic.List[string]
      $seen = New-Object System.Collections.Generic.HashSet[string]
      foreach ($ln in $prev.body) { if (-not $seen.Contains($ln)) { $merged.Add($ln); $null=$seen.Add($ln) } }
      foreach ($ln in $b.body)    { if (-not $seen.Contains($ln)) { $merged.Add($ln); $null=$seen.Add($ln) } }
      $prev.title = $b.title
      $prev.body  = $merged.ToArray()
      $map[$key] = $prev
    } else {
      $map[$key] = $b
    }
  }
  return $map.Values
}

function Augment($steps) {
  foreach ($s in $steps) {
    $t = $s.title.ToLower()
    $extra = @()
    if ($t -match "overlay|gate|erep|policy|acceptance") {
      $extra += "## Ensure overlays & gates present"
      $extra += "```powershell"
      $extra += 'git add 00_repo\.cbr\erep_policy.overlay.*.json 00_repo\.cbr\acceptance_gates*.yaml 00_repo\.cbr\erep_hooks.yaml'
      $extra += 'git commit -m "chore(erep): update overlays/gates/hooks"'
      $extra += "```"
    }
    if ($t -match "discovery|synthesis|iis|erip|ingest") {
      $extra += "## Post-discovery INBOX drain"
      $extra += "```powershell"
      $extra += 'powershell -ExecutionPolicy Bypass -File .\scripts\inbox_after_ingest.ps1'
      $extra += "```"
    }
    if ($t -match "package|snapshot|manifest|seal|full package") {
      $extra += "## Dry-run ops debt audit"
      $extra += "```powershell"
      $extra += 'powershell -ExecutionPolicy Bypass -File .\scripts\ops_debt_audit.ps1'
      $extra += "```"
    }
    if ($extra.Count -gt 0) { $s.body += ""; $s.body += $extra }
  }
  return $steps
}

function Extract-Cheatsheet($text) {
  $lines = $text -split "`n"
  $in = $false
  $buf = @()
  $blocks = @()
  foreach ($ln in $lines) {
    if ($ln -match "^\s*```(.*)$") {
      if (-not $in) { $in = $true; $buf = @() } else { $blocks += ($buf -join "`n"); $in=$false; $buf=@() }
      continue
    }
    if ($in) { $buf += $ln }
  }
  return $blocks
}

function Emit($steps, $rawText) {
  $repo = (Get-Location).Path
  $runbook = Join-Path $repo "13_OpsLog\ROADMAP\MASTER_RUNBOOK.md"
  $csv = Join-Path $repo "13_OpsLog\TODO\enerqis_steps.csv"
  $report = Join-Path $repo "00_repo\.cbr\reports\ioss_report.json"
  $progress = Join-Path $repo "13_OpsLog\ROADMAP\PROGRESS\PROGRESS_TRACKER.md"
  $cheats = Join-Path $repo "13_OpsLog\ROADMAP\TECH_OPS\tech_ops_cheatsheet.md"

  foreach ($s in $steps) { $s.stage = StageRank $s.title }
  $ordered = $steps | Sort-Object -Property @{Expression="stage";Descending=$false}, @{Expression="title";Descending=$false}

  # Runbook
  $md = @("# MASTER RUNBOOK (IOSS) — v1.1","Updated: " + (Get-Date).ToString("yyyy-MM-dd HH:mm)"),"")
  $grp = $ordered | Group-Object stage
  foreach ($g in $grp) {
    $md += "## Stage " + $g.Name
    foreach ($s in $g.Group) {
      $md += "### " + $s.title
      $md += "```powershell"
      $md += ($s.body -join "`n")
      $md += "```"
      $md += ""
    }
  }
  New-Item -ItemType Directory -Force -Path (Split-Path $runbook) | Out-Null
  $md -join "`n" | Set-Content -Encoding utf8 $runbook

  # CSV
  $header = "id,stage,title,status,priority,requires,notes,last_updated"
  $rows = @()
  $i=1
  foreach ($s in $ordered) {
    $id = "S{0:04d}" -f $i
    $title = $s.title.Replace('"','""')
    $rows += '{0},{1},"{2}",todo,P1,,"",{3}' -f $id,$s.stage,$title, (Get-Date).ToString("s")
    $i++
  }
  New-Item -ItemType Directory -Force -Path (Split-Path $csv) | Out-Null
  ($header + "`n" + ($rows -join "`n")) | Set-Content -Encoding utf8 $csv

  # Progress
  $cur = $ordered | Select-Object -First 1
  $nxt = $ordered | Select-Object -Skip 1 -First 5
  $pt = "# 📍 Progress tracker (IOSS)`n`n**Done**`n`n- _(add as you finish steps)_`n`n**Current step**`n`n1) {cur}`n`n**Next**`n".Replace("{cur}", $cur.title)
  $k=1; foreach ($n in $nxt) { $pt += ("{0}) {1}`n" -f $k, $n.title); $k++ }
  New-Item -ItemType Directory -Force -Path (Split-Path $progress) | Out-Null
  $pt | Set-Content -Encoding utf8 $progress

  # Cheatsheet
  $blocks = Extract-Cheatsheet -text $rawText
  $cs = "# Tech Ops Cheatsheet (auto-generated by IOSS)`nUpdated: " + (Get-Date).ToString("yyyy-MM-dd HH:mm") + "`n`n"
  foreach ($b in $blocks) { $cs += "```powershell`n" + $b + "`n````n" }
  New-Item -ItemType Directory -Force -Path (Split-Path $cheats) | Out-Null
  $cs | Set-Content -Encoding utf8 $cheats

  # Report
  $obj = [pscustomobject]@{
    timestamp = (Get-Date).ToString("o")
    input = $Input
    steps = $ordered.Count
    runbook = "13_OpsLog/ROADMAP/MASTER_RUNBOOK.md"
    csv = "13_OpsLog/TODO/enerqis_steps.csv"
    progress = "13_OpsLog/ROADMAP/PROGRESS/PROGRESS_TRACKER.md"
    cheatsheet = "13_OpsLog/ROADMAP/TECH_OPS/tech_ops_cheatsheet.md"
  }
  New-Item -ItemType Directory -Force -Path (Split-Path $report) | Out-Null
  $obj | ConvertTo-Json -Depth 6 | Set-Content -Encoding utf8 $report
  Write-Host "IOSS v1.1 complete: $($ordered.Count) steps -> runbook/steps/progress/cheatsheet"
}

$text = Read-AllText -p $Input
$blocks = Extract-Steps -text $text
$merged = Merge-Dups -blocks $blocks
$aug = Augment -steps $merged
Emit -steps $aug -rawText $text
