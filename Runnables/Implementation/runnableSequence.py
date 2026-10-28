# RunnableSequence is a sequential chain of runnables in LangChain that executes each step one after another, passing the output of one step as the input to the next.
# It is useful when you need to compose multiple runnables together in a structured workflow.

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openrouter import ChatOpenRouter
from langchain_core.runnables import RunnableSequence


load_dotenv()

model1 = ChatOpenRouter(
    model="nvidia/nemotron-3.5-super-vl:free",
    temperature=0.7,
    # max_tokens=500,
)

model2 = ChatOpenRouter(
    model="nvidia/nemotron-3-ultra-550b-a55b:free",
    temperature=0.8,
)

prompt1 = PromptTemplate(
    template = "Give a joke on {topic}",
    input_variables = ["topic"]
)

prompt2 = PromptTemplate(
    template = "Explain the {joke} breifly",
    input_variables = ["joke"]
)

parser = StrOutputParser()

chain = RunnableSequence(prompt1, model1, parser, prompt2, model2, parser)
result = chain.invoke({"topic": "Agentic AI"})
print(result)