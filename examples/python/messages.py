"""Send one message with the official Anthropic SDK pointed at Ebtekar."""
import os

import anthropic

client = anthropic.Anthropic(
    api_key=os.environ["EBTEKAR_API_KEY"],
    base_url="https://ebtekarai.ir/api/developer-gateway",
    default_headers={"User-Agent": "Ebtekar-Client/1.0"},
)

message = client.messages.create(
    model="ebtekar-smart",
    max_tokens=1024,
    system="تو یک دستیار صمیمی هستی و فارسی جواب می‌دهی.",
    messages=[{"role": "user", "content": "سه ایده برای یک استارتاپ کوچک بده."}],
)

print(message.content[0].text)
print("\n— usage:", message.usage.input_tokens, "in /", message.usage.output_tokens, "out")
