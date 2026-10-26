# Condition Based chains like the condition constitutes the execution of chains (mostly used in agents)

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_openrouter import ChatOpenRouter
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal


load_dotenv()

model = ChatOpenRouter(
    model="nvidia/nemotron-3.5-super-vl:free",
    temperature=0.7,
    # max_tokens=500,
)


class Feedback(BaseModel):
    sentiment : Literal["Positive", "Negative"] = Field(description = "Give the sentiment of the feedback")

parser1 = StrOutputParser()
parser2 = PydanticOutputParser(pydantic_object = Feedback)

# Defining Prompt
prompt1 = PromptTemplate(
    template = "Classify the sentiment of the {feedback}\n {format_instruction}",
    input_variables = ["feedback"],
    partial_variables = {"format_instruction" : parser2.get_format_instructions()}
)

classifier_chain = prompt1 | model | parser2


prompt2 = PromptTemplate(
    template = "Write an appropriate response to this positive feedback \n {feedback}",
    input_variables = ["feedback"]
)

prompt3 = PromptTemplate(
    template = "Write an appropriate response to this negative  feedback \n {feedback}",
    input_variables = ["feedback"]
)


branch_chain = RunnableBranch(
    (lambda x: x.sentiment == "Positive", prompt2 | model | parser1),
    (lambda x: x.sentiment == "Negative", prompt3 | model | parser1),
    RunnableLambda(lambda x: "Could not find sentiment"),# A default chain is put in case no condition is met
)

chain = classifier_chain | branch_chain

result = chain.invoke({"feedback": "What a splendid battery this mobile has!"})

print(result)