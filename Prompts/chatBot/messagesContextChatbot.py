from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openrouter import ChatOpenRouter
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenRouter(
    model= "nvidia/nemotron-3.5-lightning:free",
    temperature=0.7,
)

messages = [
    SystemMessage(content = "You are a University Professor"),
    HumanMessage(content = "What is difference between Langchain and LangGraph. Tell me in less than 25 words")
]

result = model.invoke(messages)
messages.append(AIMessage(content = result.content))

print(messages)