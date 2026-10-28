# Runnable Lambda is a runnable primitive that allows you to apply custom Pyhton functions within an AI Agents
# It acts as a middleware between different AI components, enabling preprocessing, transformation, API calls, filtering, and post-processing in a LangChain workflows
# Like You want to count the number of words in a document that you can't be doing with AI it will have innacurate results but instead make a static fucntion and make the fuction then runnable so that it can now interact with other runnables.



from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openrouter import ChatOpenRouter
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda


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
    template = "Give a joke on {topic}",
    input_variables = ["topic"]
)

prompt2 = PromptTemplate(
    template = "Explain the {joke} briefly",
    input_variables = ["joke"]
)

parser = StrOutputParser()

chain = RunnableSequence(prompt1, model1, parser, RunnableParallel({
                                                            "JOKE": RunnablePassthrough(),
                                                            "EXPLANATION":RunnableSequence(prompt2, model2, parser),
                                                            "word_count":RunnableLambda(word_counter)
                                                                })
)

chain.get_graph().print_ascii()

result = chain.invoke({"topic": "India"}) # sigle input to both the runnbles

print(f"""Joke: {result["JOKE"]} \nWords in the Joke: {result["word_count"]}""")