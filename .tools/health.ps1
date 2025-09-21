param()

git fetch -p origin | Out-Null

$ok=$true
function OK($l,$p){ if(-not $p){$script:ok=$false}; "{0} {1}" -f ($(if($p){"✅"}else{"❌"}),$l) }

$onMain  = (git rev-parse --abbrev-ref HEAD).Trim() -eq 'main'
$sync    = (git rev-parse HEAD).Trim() -eq (git rev-parse origin/main).Trim()
git diff-index --quiet HEAD --; $clean=$?

$hasPre   = Test-Path .github/workflows/pre-commit.yml
$hasEREP  = (Test-Path .github/workflows/erep.yml) -and (Test-Path .github/workflows/erep-guard.yml) -and (Test-Path .github/workflows/erep_equivalence.yml)
$hasDep   = Test-Path .github/dependabot.yml
$hasAuto  = Test-Path .github/workflows/dependabot-auto-merge.yml
$hasOwners= Test-Path .github/CODEOWNERS
$hasEditor= Test-Path .editorconfig
$hasSec   = Test-Path SECURITY.md
$readmeHas= Select-String -Path README.md -Pattern '\[Code scanning \(CodeQL\)\]\(\.\.\/\.\.\/security\/code-scanning\)' -Quiet

OK "on branch 'main'"                      $onMain
OK "main == origin/main"                   $sync
OK "working tree clean"                    $clean
OK "pre-commit workflow present"           $hasPre
OK "EREP workflows present"                $hasEREP
OK "Dependabot config present"             $hasDep
OK "Auto-merge helper present"             $hasAuto
OK "CODEOWNERS present"                    $hasOwners
OK ".editorconfig present"                 $hasEditor
OK "SECURITY.md present"                   $hasSec
OK "README uses CodeQL link (stable)"      $readmeHas

# Remote gate probe (safe: push is rejected)
$probe = "tmp/probe-" + (Get-Date -Format "yyyyMMdd-HHmmss")
git switch -c $probe origin/main | Out-Null
git commit --allow-empty -S -m "probe: gates" | Out-Null
$pushOut = git push -u origin HEAD:main 2>&1
git switch main | Out-Null
git branch -D $probe | Out-Null

$g013      = $pushOut -match 'GH013'
$prOnly    = $pushOut -match 'Changes must be made through a pull request'
$codeqlReq = $pushOut -match 'Code scanning is waiting for results from CodeQL'

OK "Remote gates (PR-only) enforced"       ($g013 -and $prOnly)
OK "Remote gates include CodeQL required"  ($g013 -and $codeqlReq)

if ($ok) { Write-Host "`n✅ Everything is 100% set." -ForegroundColor Green }
else      { Write-Host "`n⚠️  Something above needs attention." -ForegroundColor Yellow; $pushOut }
