from langchain_openrouter import ChatOpenRouter
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenRouter(
    model = "apodex/apodex-1.1-mini:free",
    temperature = 1.5, # 0-2; Creativity level
)

result = model.invoke("Write me a poem on the stoic life of a soldier? Answer in max 5 lines")
print(result.content)