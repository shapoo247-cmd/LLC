#!/usr/bin/env bash
# Rebuilds the full videos from their <50 MB parts and verifies them byte-for-byte.
# Run once after cloning:  bash setup.sh
set -euo pipefail
cd "$(dirname "$0")"

cat footage/parts/raw_footage_1.mp4.part*   > footage/raw_footage_1.mp4
cat reference/parts/sample_llc_1.mp4.part*  > reference/sample_llc_1.mp4

sha256sum -c SHA256SUMS
echo "Videos ready: footage/raw_footage_1.mp4, reference/sample_llc_1.mp4"
