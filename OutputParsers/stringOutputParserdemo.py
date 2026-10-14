# Output like : 'ChatHuggingFace' object has no attribute 'with_structured_Structured'. Did you mean: 'with_structured_output'?

from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = HuggingFacePipeline.from_model_id(
    model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task = "text-generation",
    pipeline_kwargs = {
        "max_length": 512,
        "temperature": 0.7
    }
)

model = ChatHuggingFace(llm = llm )

# template 1
template1 = PromptTemplate(
    template = "Write a 3 line summary on the {topic}",
    input_variables = ["topic"]
)

# template 2
template2 = PromptTemplate(
    template = "Explain the concept of {text} in a quotidian manner",
    input_variables = ["text"]
)
    
prompt1 = template1.invoke({"topic": "poverty"}) # or format
result1 = model.invoke(prompt1)
    
prompt2 = template2.format(text = result1.content)
result2 = model.invoke(prompt2)

print(result2.content)