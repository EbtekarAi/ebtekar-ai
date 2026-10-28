#!/usr/bin/env bash
# Stream a response as Server-Sent Events.
set -euo pipefail
: "${EBTEKAR_API_KEY:?Set EBTEKAR_API_KEY first}"
BASE="https://ebtekarai.ir/api/developer-gateway"

curl -sN "$BASE/v1/messages" \
  -H "x-api-key: $EBTEKAR_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "content-type: application/json" \
  -d '{
    "model": "ebtekar-smart",
    "max_tokens": 1024,
    "stream": true,
    "messages": [{"role": "user", "content": "یک شعر کوتاه دربارهٔ باران بنویس"}]
  }'
