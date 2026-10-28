// Send one message with the official Anthropic SDK pointed at Ebtekar.
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env.EBTEKAR_API_KEY,
  baseURL: "https://ebtekarai.ir/api/developer-gateway",
});

const msg = await client.messages.create({
  model: "ebtekar-smart",
  max_tokens: 1024,
  messages: [{ role: "user", content: "سلام! یک نقل‌قول انگیزشی کوتاه بگو." }],
});

console.log(msg.content[0].text);
console.log(`— usage: ${msg.usage.input_tokens} in / ${msg.usage.output_tokens} out`);
