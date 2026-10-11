import json
from urllib.request import Request, urlopen

from dotenv import dotenv_values

api_key = dotenv_values().get("OPENROUTER_API_KEY")
if not api_key:
    raise ValueError("Set OPENROUTER_API_KEY in your .env file.")

request = Request(
    "https://openrouter.ai/api/v1/embeddings",
    data=json.dumps(
        {
            "model": "nvidia/llama-nemotron-embed-vl-1b-v2:free",
            "input": "What is the capital of Egypt?",
        }
    ).encode(),
    headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    },
    method="POST",
)

with urlopen(request) as response:
    result = json.load(response)

print(result["data"][0]["embedding"])