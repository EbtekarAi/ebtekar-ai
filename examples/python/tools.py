"""Tool use: the model asks for a tool, your code runs it, the model answers.

The gateway never executes tools. Validate inputs and keep side effects on your side.
"""
import json
import os

import anthropic

client = anthropic.Anthropic(
    api_key=os.environ["EBTEKAR_API_KEY"],
    base_url="https://ebtekarai.ir/api/developer-gateway",
)

TOOLS = [{
    "name": "get_weather",
    "description": "Get the current weather for a city",
    "input_schema": {
        "type": "object",
        "properties": {"city": {"type": "string"}},
        "required": ["city"],
    },
}]


def get_weather(city: str) -> str:
    # Replace with a real lookup. Always validate `city` before using it.
    return json.dumps({"city": city, "temp_c": 21, "sky": "clear"}, ensure_ascii=False)


messages = [{"role": "user", "content": "هوای شیراز الان چطوره؟"}]
resp = client.messages.create(model="ebtekar-smart", max_tokens=1024, tools=TOOLS, messages=messages)

while resp.stop_reason == "tool_use":
    messages.append({"role": "assistant", "content": resp.content})
    results = []
    for block in resp.content:
        if block.type == "tool_use" and block.name == "get_weather":
            city = str(block.input.get("city", ""))[:80]
            results.append({"type": "tool_result", "tool_use_id": block.id, "content": get_weather(city)})
    messages.append({"role": "user", "content": results})
    resp = client.messages.create(model="ebtekar-smart", max_tokens=1024, tools=TOOLS, messages=messages)

print(next((b.text for b in resp.content if b.type == "text"), ""))
