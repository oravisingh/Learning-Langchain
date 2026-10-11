from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from dotenv import load_dotenv

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

result = model.invoke( # You can use .batch to ask multiple questions at once
    "What were they trying to imply in the inceeption movie?"
    
    )
print(result.content)