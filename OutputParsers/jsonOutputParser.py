from langchain_openrouter import ChatOpenRouter
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

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
parser = JsonOutputParser()

template= PromptTemplate(
    template = "Write briefly about some components on {topic} \n {format_instruction}",
    input_variables = ["topic"],
    partial_variables = {"format_instruction" : parser.get_format_instructions()} # partial variables are those which come at the runtime unlike userinput

)  

# prompt = template.format(topic = "AGI")

# print(prompt)

# result = model.invoke(prompt)
# finalResult = parser.parse(result.content)

# OR

chain = template | model | parser # here you see this automatically calling and producing the output in JSON format
finalResult = chain.invoke({"AGI"})

print(finalResult)

# but with JSON Output parser you cannot have defined schema of your choice the LLm will itself decide for that 
# or JsonOutputParse does not enfore schema