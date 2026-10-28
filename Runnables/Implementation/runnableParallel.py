# Runnable Parallel is a runnable primitive that allowsmultiple runnables to execute in parallel
# Each runnable receives the same input and processes it independently, producing a dictionary of outputs.

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openrouter import ChatOpenRouter
from langchain_core.runnables import RunnableSequence, RunnableParallel


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
    template = "Generate a twitter post on {topic}",
    input_variables = ["topic"]
)

prompt2 = PromptTemplate(
    template = "Generate a linkedin post on {topic}",
    input_variables = ["topic"]
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    "TWEETER": RunnableSequence(prompt1, model1, parser),
    "LINKEDIN":RunnableSequence(prompt2, model1, parser)
})

result = parallel_chain.invoke({"topic": "Agentic AI"}) # sigle input to both the runnbles

print(result)