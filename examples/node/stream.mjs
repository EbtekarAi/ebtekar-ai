// Stream a response as it is generated.
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env.EBTEKAR_API_KEY,
  baseURL: "https://ebtekarai.ir/api/developer-gateway",
});

const stream = await client.messages.stream({
  model: "ebtekar-smart",
  max_tokens: 2048,
  messages: [{ role: "user", content: "یک شعر کوتاه دربارهٔ پاییز بنویس." }],
});

for await (const event of stream) {
  if (event.type === "content_block_delta") process.stdout.write(event.delta.text || "");
}
process.stdout.write("\n");
