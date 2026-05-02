from dotenv import load_dotenv
import anthropic
import os

load_dotenv()

client = anthropic.Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

message = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=50,
    messages=[{
        "role": "user",
        "content": "Say exactly: Day 0 complete. Ready to build."
    }]
)

print(message.content[0].text)