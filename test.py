from dotenv import load_dotenv
from langchain_openrouter import ChatOpenRouter

load_dotenv()

model = ChatOpenRouter(
    model="openrouter/free",
    temperature=0,
)

response = model.invoke("Reply with: OpenRouter is working!")
print(response.content)