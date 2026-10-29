# Document Loaders are components in LangChain used to load data from various sources into a standardized format( usually Document Objects),
# which can then be used for chunking embedding, retrieval and augumentation.

# Document(
# page_content ="The Actual text content",
# meta_data = {"source": "filename.pdf", ...})

### Text Loader ###
# TextLoader is a simple and commonly used document loader in LangChain that reads plain text (.txt) files and converts them into LangChain Document Objects.

## Use Cases
# Ideal for loading chat logs, scraped text, transcripts, code snippets, or any plain text data into a Langchain Pipeline

## Limitation 
# Works only with .txt files


from langchain_community.document_loaders import TextLoader   
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

loader = TextLoader("Loader/election.txt",encoding = "utf-8")
docs = loader.load()

# print(docs)
# print(type(docs)) # List
# print(type(docs[0])) # Document Object
# print(docs[0].page_content) # Document Object
# print(len(docs))

chain =  prompt1 | model1 | parser

print(chain.invoke({"text": docs}))