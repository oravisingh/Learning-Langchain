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
    "Why did the chicken cross the road?",
    "To get to the other side.",
    "Why is the sky blue?",
    "Because the ocean spilled its paint.",
    "What is a ghost's favorite color?",
    "Boo!",
    "Why do fish live in water?",
    "Because they don't have Wi-Fi.",
    "What do you call a lazy kangaroo?",
    "A pouch potato.",
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



class NakliPromptTemplate():
    def __init__(self, template, input_variables):
        self.template = template
        self.input_variables = input_variables

    def invoke(self, input_dict):
        return self.template.format(**input_dict)

    def format(self, input_dict):
        return self.template.format(**input_dict)




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


# Using all above modules here to use them all at once since they all are standardized

class RunnableConnector(Runnable):
    def __init__(self, runnable_list):
        self.runnable_list = runnable_list

    def invoke(self, input_data):

        for runnable in self.runnable_list:
            input_data = runnable.invoke(input_data)

        return input_data


template1 = NakliPromptTemplate(
    template = "Write a joke about {topic}",
    input_variables = ["topic"]
)

template2 = NakliPromptTemplate(
    template = "Write a summary about the following joke\n {joke}",
    input_variables = ["joke"]
)


llm = NakliLLM()


parser = NakliStrOutput()

chain1 = RunnableConnector([template1, llm])

chain2 = RunnableConnector([template2, llm, parser])

finalChain = RunnableConnector([chain1, chain2])

print(finalChain.invoke("topic": "Birds"))
