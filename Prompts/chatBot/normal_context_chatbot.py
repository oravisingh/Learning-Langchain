from dotenv import load_dotenv
from langchain_openrouter import ChatOpenRouter

load_dotenv()

model = ChatOpenRouter(
    model = "nvidia/nemotron-3.5-lightning:free",
    temperature=0.7,
)

chat_context = []

while True:
    user_input = input("You: ")
    chat_context.append({"role": "user", "content": user_input}) # Like this we need labelling as well in the chat history for that we have messages in LangChain

    if user_input.lower() in ["exit", "quit"]:
        print("Exiting the chatbot. Goodbye!")
        break
    response = model.invoke(chat_context)
    chat_context.append({'role': "assistant", "content": response.content})
    print("Chatbot:", response.content)

print(chat_context)  # Print the entire chat context for reference



### Contextless chatbot code snippet
    # user_input = input("You: ")
    # if user_input.lower() in ["exit", "quit"]:
    #     print("Exiting the chatbot. Goodbye!")
    #     break
    # response = model.invoke(user_input)
    # print("Chatbot:", response.content)