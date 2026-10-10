from dotenv import load_dotenv
from langchain_openrouter import ChatOpenRouter

load_dotenv()

llm = ChatOpenRouter(
    model = "nvidia/nemotron-3.5-lightning:free", # It is an LLM
    temperature = 0
)

result = llm.invoke("How old was Gandhi ji when he died?")

print(result.content)