param([string]$CsvPath="13_OpsLog\TODO\enerqis_backlog.csv",[string]$OutCsv="13_OpsLog\TODO\enerqis_backlog_ranked.csv")
if(!(Test-Path $CsvPath)){ Write-Error "Backlog CSV not found: $CsvPath"; exit 1 }
$rows=Import-Csv $CsvPath
foreach($r in $rows){
  $reach=[double]$r.reach; $impact=[double]$r.impact; $conf=[double]$r.confidence; $effort=[double]$r.effort
  if($effort -le 0){ $effort=0.5 }
  $r.rice=[math]::Round(($reach*$impact*$conf)/$effort,3)
}
$rows | Sort-Object {[double]$_.rice} -Descending | Export-Csv -Path $OutCsv -NoTypeInformation
"Ranked backlog written to $OutCsv"
