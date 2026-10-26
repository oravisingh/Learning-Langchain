# Runnable automates the manual tasks
import random

class NakliLLM():
    def __init__(self):
        print("LLM Created")

    def predict(self,prompt):
        responseList = [
            "Delhi is the capital of India",
            "IPL is a cricket league",
            "AI stands for Artificial Intelligence"
        ]

        return {"Response" : random.choice(responseList)}

llm = NakliLLM()

print(llm.predict("What is the Capital of India?"))


class NakliPromptTemplate():
    def __init__(self, template, input_variables):
        self.template = template
        self.input_variables = input_variables

    def format(self, input_dict):
        return self.template.format(**input_dict)

template = NakliPromptTemplate(
    template = "Write a {length} poem on {topic}",
    input_variables = ["topic", "length"]
)

prompt = template.format({"topic":"Birds", "length": "short"})
print(prompt)

# Calling the naklillm with the nakli prompt

print(llm.predict(prompt))