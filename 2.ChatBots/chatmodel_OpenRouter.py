from pathlib import Path
from dotenv import load_dotenv
from langchain_openrouter import ChatOpenRouter

env_path = Path(__file__).resolve().parents[1] / ".env"
load_dotenv(env_path, override=True)

model = ChatOpenRouter(
    model="nvidia/nemotron-3-super-120b-a12b:free",
    temperature=0.7,
    # max_tokens=500,
)

result = model.invoke(
    "What is the BMI of a person 188cm and 144lb?"
)

print(result.content)