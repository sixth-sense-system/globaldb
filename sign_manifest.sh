#!/usr/bin/env bash
set -euo pipefail
WR="${1:-ENERQIS_GlobalDB}"
MAN="$WR/00_repo/.cbr/out/manifest-sha256.txt"
if [[ ! -f "$MAN" ]]; then echo "manifest-sha256.txt not found under $WR"; exit 1; fi
echo "Signing $MAN with GPG (detached, armored)"
gpg --batch --yes --armor --output "$MAN.asc" --detach-sign "$MAN"
echo "Signature wrote to $MAN.asc"
gpg --verify "$MAN.asc" "$MAN" || { echo "Verify failed"; exit 1; }
echo "Signature verified."
