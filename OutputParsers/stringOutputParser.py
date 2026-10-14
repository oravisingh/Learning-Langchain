from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = HuggingFacePipeline.from_model_id(
    model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task = "text-generation",
    pipeline_kwargs = {
        "max_length": 1024,
        "temperature": 0.7
    }
)

model = ChatHuggingFace(llm = llm )

# template 1
template1 = PromptTemplate(
    template = "Toss a single topic in the field of {field}",
    input_variables = ["field"]
)

# template 2
template2 = PromptTemplate(
    template = "Explain the full scenario of {text}",
    input_variables = ["text"]
)

# The StringOutputParser that extracts the structured output from a raw LLm response
parser = StrOutputParser() # the string output


# Chain Formation
chain = template1 | model | parser | template2 | model | parser # The parser here makes the chain possible since It gives a direct structured output  which is then fed forward

result = chain.invoke({"field":"geopolitics"})

print(result)
