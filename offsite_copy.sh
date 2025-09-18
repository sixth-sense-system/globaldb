#!/usr/bin/env bash
set -euo pipefail
if [[ $# -lt 2 ]]; then
  echo "Usage: $0 <ZIP_PATH> <S3_URI>"
  echo "Example: $0 ENERQIS_20250912-2030_repo.zip s3://enerqis-baselines/2025/09/"
  exit 2
fi
ZIP="$1"; DEST="$2"
aws s3 cp "$ZIP" "$DEST" --storage-class GLACIER_IR --no-progress
echo "Copied to $DEST"
