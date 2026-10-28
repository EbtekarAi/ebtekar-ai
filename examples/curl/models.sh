#!/usr/bin/env bash
# List the text models available to your key.
set -euo pipefail
: "${EBTEKAR_API_KEY:?Set EBTEKAR_API_KEY first}"

curl -sS "https://ebtekarai.ir/api/developer-gateway/v1/models" \
  -H "x-api-key: $EBTEKAR_API_KEY" \
  -H "anthropic-version: 2023-06-01"
echo
