from dotenv import dotenv_values
from langchain_openai import OpenAIEmbeddings

api_key = dotenv_values().get("OPENROUTER_API_KEY")
if not api_key:
    raise ValueError("Set OPENROUTER_API_KEY in your .env file.")

embeddings = OpenAIEmbeddings(
    model="nvidia/llama-nemotron-embed-vl-1b-v2:free",
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
    check_embedding_ctx_length=False,
)

vector = embeddings.embed_query("What is the capital of Egypt?")
print(str(vector))