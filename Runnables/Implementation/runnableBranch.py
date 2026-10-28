# Runnable Branch is a control flow component in a LangChain that allows you to conditionally route input data to diffrent chains or runnables based on custom logic.
# It functions like an if/else/elif block for chains - where you define a set of condition functions, each associated witha arunnable(e.g. LLM Call, Prompt Chain or a tool).
# The first matching condition is executed if. If no condition matches, a default runnable is used(if provided).

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openrouter import ChatOpenRouter
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda, RunnableLambda, RunnableBranch


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

def word_counter(text):
    return len(text.split())

runnable_word_counter = RunnableLambda(word_counter)
# text = "I want to live such a life where I am able to help everyone in the best way possible"
# print(runnable_word_counter.invoke(text))

prompt1 = PromptTemplate(
    template = "Write a detailed report on {topic}",
    input_variables = ["topic"]
)

prompt2 = PromptTemplate(
    template = "Summarize the following {text}",
    input_variables = ["text"]
)

parser = StrOutputParser()

report_gen_chain = RunnableSequence(prompt1, model1, parser)

branch_chain = RunnableBranch(
    (lambda x: len(x.split()) > 500, RunnableSequence(prompt2, model1, parser)),
    (RunnablePassthrough()),
    )

final_chain = RunnableSequence(report_gen_chain, branch_chain)

# LCEL: LangChain Expression Language
# Another shorter way to use RunnableSequence
# RunnableSequence(report_gen_chain, branch_chain) --> [report_gen_chain | branch_chain]


result = final_chain.invoke({"topic": "India"}) # sigle input to both the runnbles
print(result)

final_chain.get_graph().print_ascii()
