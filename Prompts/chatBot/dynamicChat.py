from langchain_openrouter import ChatOpenRouter
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

model = ChatOpenRouter(
    model= "nvidia/nemotron-3.5-lightning:free",
    temperature=0.7,
)

chatTemplate = ChatPromptTemplate([ # there is a peculiar way here to assign to systemmessage, aimessage and humanmessage
    ("system", "You're a {profession}"),
    ("human","Explain {body_part}'s fuctions")
])


prompt = chatTemplate.invoke({"profession": "Doctor", "body_part" : "liver"})

print(prompt)