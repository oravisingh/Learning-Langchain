from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_classic.output_parsers import ResponseSchema, StructuredOutputParser
from langchain_openrouter import ChatOpenRouter


load_dotenv()

model = ChatOpenRouter(
    model="nvidia/nemotron-3-super-120b-a12b:free",
    temperature=0.7,
    # max_tokens=500,
)

schema = [
    ResponseSchema(name="definition", description="Briefly define the topic"),
    ResponseSchema(
        name="components",
        description="List the main components of the topic",
    ),
    ResponseSchema(
        name="examples",
        description="Give contemporary use cases and examples",
    ),
    ResponseSchema(
        name="future_scope",
        description="Describe possible future advancements",
    ),
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template="Briefly explain {topic}.\n{format_instruction}",
    input_variables=["topic"],
    partial_variables={"format_instruction": parser.get_format_instructions()},
)

# prompt = template.invoke({"topic": "AGI"})

# result = model.invoke(prompt)

# final_result = parser.parse(result.content)

# OR

chain = template | model | parser

final_result = chain.invoke({"AGI"})

print(final_result)


# Advantages:
#     -Can force schema

# Disadvantage:
#     -Can't impose Data Validation
