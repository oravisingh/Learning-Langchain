# it also keeps standard labelled history and We chat with the full context
from dotenv import load_dotenv
from langchain_openrouter import ChatOpenRouter
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

model = ChatOpenRouter(
    model = "nvidia/nemotron-3.5-lightning:free",
    temperature=0.7,
)

chat_context = [SystemMessage(content = "You are a soldier who is also a geek")]

while True:
    user_input = input("You: ")
    chat_context.append(HumanMessage(content = user_input))

    if user_input.lower() in ["exit", "quit"]:
        print("Exiting the chatbot. Goodbye!")
        break
    response = model.invoke(chat_context)
    chat_context.append(AIMessage(content = response.content))
    print("Chatbot:", response.content)

print(chat_context)  # Print the entire chat context for reference

