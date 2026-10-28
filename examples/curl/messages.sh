#!/usr/bin/env bash
# Send one message and print the JSON response.
set -euo pipefail
: "${EBTEKAR_API_KEY:?Set EBTEKAR_API_KEY first}"
BASE="https://ebtekarai.ir/api/developer-gateway"

curl -sS "$BASE/v1/messages" \
  -H "x-api-key: $EBTEKAR_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "content-type: application/json" \
  -d '{
    "model": "ebtekar-smart",
    "max_tokens": 1024,
    "messages": [{"role": "user", "content": "سلام! در سه جمله خودت را معرفی کن."}]
  }'
echo
