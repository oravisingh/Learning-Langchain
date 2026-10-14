from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_classic.output_parsers import PydanticOutputParser
from langchain_openrouter import ChatOpenRouter
from pydantic import BaseModel, Field


load_dotenv()

# Define the model
model = ChatOpenRouter(
    model="nvidia/nemotron-3-super-120b-a12b:free",
    temperature=0.7,
    # max_tokens=500,
)

# Define the Output Structure
class Person(BaseModel):
    name: str = Field(description = "Name of a Person")
    age: int = Field(description = "It should be a young age", gt = 18, lt = 36)
    address: str = Field(description = "A prominent city")

# defining a pydantic parser
parser = PydanticOutputParser(pydantic_object = Person)

# Defining a template
template = PromptTemplate(
    template = "Generate a random profile of a young person belonging to {location}\n {format_instructions}",
    input_variables = ["location"],
    partial_variables = {"format_instructions" : parser.get_format_instructions()}

) 

# Defining the prompt
# prompt = template.format(location = "India")
# print(prompt)

# result = model.invoke(prompt)
# final_result = parser.parse(result.content)

# OR


# Creating a chain
chain = template | model | parser

final_result = chain.invoke({"location": "India"})

print(final_result)



