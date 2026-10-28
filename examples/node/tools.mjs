// Tool use loop. The gateway never runs your tools; your code does.
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env.EBTEKAR_API_KEY,
  baseURL: "https://ebtekarai.ir/api/developer-gateway",
});

const tools = [{
  name: "get_weather",
  description: "Get the current weather for a city",
  input_schema: { type: "object", properties: { city: { type: "string" } }, required: ["city"] },
}];

// Replace with a real lookup. Always validate input before using it.
const getWeather = (city) => JSON.stringify({ city, temp_c: 21, sky: "clear" });

const messages = [{ role: "user", content: "هوای اصفهان الان چطوره؟" }];
let resp = await client.messages.create({ model: "ebtekar-smart", max_tokens: 1024, tools, messages });

while (resp.stop_reason === "tool_use") {
  messages.push({ role: "assistant", content: resp.content });
  const results = resp.content
    .filter((b) => b.type === "tool_use" && b.name === "get_weather")
    .map((b) => ({ type: "tool_result", tool_use_id: b.id, content: getWeather(String(b.input.city ?? "").slice(0, 80)) }));
  messages.push({ role: "user", content: results });
  resp = await client.messages.create({ model: "ebtekar-smart", max_tokens: 1024, tools, messages });
}

console.log(resp.content.find((b) => b.type === "text")?.text ?? "");
