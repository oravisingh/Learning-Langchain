# It is a placeholder to store the chat messages
# It is used to store and retrieve chat history
import json

from langchain_core.messages import messages_from_dict
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# chat template

chatTemplate = ChatPromptTemplate([
    ("system","You are a helpful customer support agent"),
    MessagesPlaceholder(variable_name = "chat_history"),
    ("human", "{query}")
])


chat_history =[]
# load Chat history
with open("Prompts/chat_history.txt") as g:
    chat_history.extend(messages_from_dict(json.load(g)))

# create prompt
prompt = chatTemplate.invoke({"chat_history": chat_history, "query": "Where is my refund?"})
print(prompt)