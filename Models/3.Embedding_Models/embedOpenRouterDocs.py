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
    dimensions = 32
)

document = ["What is the capital of Egypt?",
            "How many continents are there on Earth?",
            "What is the largest ocean in the world?",
        
           ]

vector = embeddings.embed_documents(document)
print(str(vector),  len(vector))

print(vector)