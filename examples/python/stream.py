"""Stream a response token by token."""
import os

import anthropic

client = anthropic.Anthropic(
    api_key=os.environ["EBTEKAR_API_KEY"],
    base_url="https://ebtekarai.ir/api/developer-gateway",
    default_headers={"User-Agent": "Ebtekar-Client/1.0"},
)

with client.messages.stream(
    model="ebtekar-smart",
    max_tokens=2048,
    messages=[{"role": "user", "content": "یک داستان خیلی کوتاه دربارهٔ یک ربات مهربان بنویس."}],
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)
print()
