import random
from abc import ABC, abstractmethod

# So in a way I'm forcing the classes to follow a set of standardized rules

class Runnable(ABC):
    @abstractmethod
    def invoke(self):
        pass


class NakliLLM(Runnable):
    def __init__(self):
        print("LLM Created")

    def invoke(self,prompt):
        responseList = [
            "Delhi is the capital of India",
            "IPL is a cricket league",
            "AI stands for Artificial Intelligence"
        ]

        return {"Response" : random.choice(responseList)}

    def predict(self,prompt):
        responseList = [
            "Delhi is the capital of India",
            "IPL is a cricket league",
            "AI stands for Artificial Intelligence"
        ]
        print("This method is going to deprecate soon. Use \x1B[3m invoke() \x1B[23m instead")

        return {"Response" : random.choice(responseList)}

llm = NakliLLM()

# print(llm.invoke("What is the Capital of India?"))


class NakliPromptTemplate():
    def __init__(self, template, input_variables):
        self.template = template
        self.input_variables = input_variables

    def invoke(self, input_dict):
        return self.template.format(**input_dict)

    def format(self, input_dict):
        return self.template.format(**input_dict)

template = NakliPromptTemplate(
    template = "Write a {length} poem on {topic}",
    input_variables = ["topic", "length"]
)


class NakliLLMchain():
    def __init__(self, template, model):
        self.template = template
        self.model = model

    def invoke(self, input_data):
        prompt = self.template.format(input_data)
        return self.model.predict(prompt)["Response"]

chain = NakliLLMchain(
    template = template,
    model = llm
)


class NakliStrOutput(Runnable):
    def __init__(self):
        pass

    def invoke(self, input_data):
        self.input_data = input_data
        return input_data["Response"]

parser = NakliStrOutput()

# Using all above modules here to use them all at once since they all are standardized

class RunnableConnector(Runnable):
    def __init__(self, runnable_list):
        self.runnable_list = runnable_list

    def invoke(self, input_data):

        for runnable in self.runnable_list:
            input_data = runnable.invoke(input_data)

        return input_data

chain1 = RunnableConnector([template, llm, parser])

print(chain1.invoke({"topic":"Birds", "length": "short"}))