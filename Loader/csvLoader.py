from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader, CSVLoader
from langchain_openrouter import ChatOpenRouter
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

parser = StrOutputParser()

model1 = ChatOpenRouter(
    model="nvidia/nemotron-3.5-super-vl:free",
    temperature=0.7,
    # max_tokens=500,
)

prompt1 = PromptTemplate(
    template = " Write a quick summary on {text}",
    input_variables = ["text"]

)

loader = CSVLoader(file_path = "Loader/large-dataset.csv" )

docs = loader.load() 


# print(docs)
print(type(docs)) # List
print(type(docs[0])) # Document Object
print(len(docs))
print(docs[0].metadata)

chain = prompt1 | model1 | parser

print(chain.invoke({"text": docs}))

