# Runnable Passthrough is a special Runnable Primitive that simply returns the input as well as output without modifying it.
# It is used when you just need the exact text even wehen passing the text through a Runnable
# Like generating the joke as well as the explaination as in the first example we were not getting the JOke itself but the explanation only

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openrouter import ChatOpenRouter
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough


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
    template = "Explain the {joke} briefly",
    input_variables = ["joke"]
)

print(RunnablePassthrough().invoke("Just the input return"))

parser = StrOutputParser()

chain = RunnableSequence(prompt1, model1, parser, RunnableParallel({
                                                            "JOKE": RunnablePassthrough(),
                                                            "EXPLANATION":RunnableSequence(prompt2, model2, parser)
                                                                })
)

result = chain.invoke({"topic": "Agentic AI"}) # sigle input to both the runnbles

print(result)