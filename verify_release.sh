#!/usr/bin/env bash
set -euo pipefail
if [[ $# -lt 2 ]]; then
  echo "Usage: $0 <ZIP_PATH> <EXPECTED_ARCHIVE_SHA256>"
  exit 2
fi
ZIP="$1"
EXP="$2"
echo "== Verify archive SHA-256 =="
ACT=$(sha256sum "$ZIP" | awk '{print $1}')
echo "Archive SHA256: $ACT"
if [[ "$ACT" != "$EXP" ]]; then
  echo "Mismatch!"; exit 1
fi
echo "OK"

echo "== Extract and verify internal manifest =="
TMP=$(mktemp -d)
unzip -q "$ZIP" -d "$TMP"
WR="$TMP/ENERQIS_GlobalDB"
if [[ ! -d "$WR" ]]; then echo "Wrapper missing"; exit 1; fi

MAN="$WR/00_repo/.cbr/out/manifest-sha256.txt"
if [[ ! -f "$MAN" ]]; then echo "manifest-sha256.txt missing"; exit 1; fi
MANVAL=$(cat "$MAN")

# recompute canonical manifest
EXCL1="00_repo/.cbr/out/manifest-sha256.txt"
EXCL2="00_repo/.cbr/reports/filelist_manifest.txt"
mapfile -t FILES < <(cd "$WR" && find . -type f ! -path "./$EXCL1" ! -path "./$EXCL2" | sed 's|^\./||' | LC_ALL=C sort)
MAN_TXT=""
for f in "${FILES[@]}"; do
  SZ=$(stat -c%s "$WR/$f")
  H=$(sha256sum "$WR/$f" | awk '{print $1}')
  MAN_TXT+="$f\t$SZ\t$H"$'\n'
done
RECOMP=$(printf "%s" "$MAN_TXT" | sha256sum | awk '{print $1}')

echo "Manifest inside:    $MANVAL"
echo "Manifest recompute: $RECOMP"
if [[ "$MANVAL" != "$RECOMP" ]]; then
  echo "Manifest mismatch!"; exit 1
fi
echo "Manifest OK"
