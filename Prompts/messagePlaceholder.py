from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# chat template

chatTemplate = ChatPromptTemplate([
    ("system","You are a helpful customer support agent"),
    MessagesPlaceholder(variable_name = "chat_history"),
    ("human", "{query}")
])


chat_history =[]
# load Chat history
with open("chat_history.txt") as g:
    chat_history.extend(g.readlines())

# create prompt
prompt = chatTemplate.invoke({"chat_history": chat_history, "query": "Where is my refund?"})