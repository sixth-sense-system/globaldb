param(
  [Parameter(Mandatory=$true)][string]$Title,
  [string]$Type="Idea",[string]$Theme="",[string]$Status="Inbox",[string]$Priority="P2",
  [double]$Reach=1,[double]$Impact=5,[double]$Confidence=0.6,[double]$Effort=1,
  [string]$Owner="ENERQIS",[string]$Due="",[string]$Source="OpsLog",[string]$Links="",[string]$Notes="")
$Csv="13_OpsLog\TODO\enerqis_backlog.csv"
if(!(Test-Path $Csv)){ Write-Error "Backlog CSV not found: $Csv"; exit 1 }
$created=Get-Date -Format "yyyy-MM-dd"
$existing=Import-Csv $Csv; $id=1
if($existing.Count -gt 0){ $id=([int]($existing | Measure-Object -Property id -Maximum).Maximum)+1 }
$eff= [double]$Effort; if($eff -le 0){ $eff=0.5 }
$rice=[math]::Round(($Reach*$Impact*$Confidence)/$eff,3)
$new=[PSCustomObject]@{{ id=$id; title=$Title; type=$Type; theme=$Theme; status=$Status; priority=$Priority;
  reach=$Reach; impact=$Impact; confidence=$Confidence; effort=$Effort; rice=$rice;
  owner=$Owner; due=$Due; created_at=$created; source=$Source; links=$Links; notes=$Notes }}
$all=@(); if($existing){{ $all+=$existing }}; $all+=$new
$all | Export-Csv -Path $Csv -NoTypeInformation
"Added backlog item #$id: $Title"
