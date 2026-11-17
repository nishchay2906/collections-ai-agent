# Collections AI agent

An initial Python scaffold with an Anthropic API smoke check. Agent workflows and application code are still to be implemented.

## Run the API smoke check

Create and activate a Python virtual environment.

```sh
python -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
```

Copy [.env.example](.env.example) to `.env` and set `ANTHROPIC_API_KEY`. Run the check explicitly from the repository root.

```sh
python tests/smoke_anthropic.py
```

The script makes one live API request and prints the reply. Set `ANTHROPIC_MODEL` to override the default model ID.
