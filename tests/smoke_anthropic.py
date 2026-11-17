"""Run an explicit Anthropic API smoke check."""

import os

import anthropic
from dotenv import load_dotenv


def main():
    load_dotenv()
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise SystemExit("Set ANTHROPIC_API_KEY in your environment or .env file.")

    client = anthropic.Anthropic(api_key=api_key)
    message = client.messages.create(
        model=os.getenv("ANTHROPIC_MODEL", "claude-haiku-4-5-20251001"),
        max_tokens=50,
        messages=[{"role": "user", "content": "Say exactly: Day 0 complete. Ready to build."}],
    )
    print("".join(block.text for block in message.content if block.type == "text"))


if __name__ == "__main__":
    main()
