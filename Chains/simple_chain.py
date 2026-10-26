from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openrouter import ChatOpenRouter


load_dotenv()

model = ChatOpenRouter(
    model="nvidia/nemotron-3.5-super-vl:free",
    temperature=0.7,
    # max_tokens=500,
)

prompt1 = PromptTemplate(
    template = "Give one random name from the {topic}",
    input_variables = ["topic"]
)

prompt2 = PromptTemplate(
    template = "Generate 5 interesting facts about {name}",
    input_variablea = ["name"]
)

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser
chain.get_graph().print_ascii()

result = chain.invoke({"topic" : "Fighter Jets"})

print(result)

