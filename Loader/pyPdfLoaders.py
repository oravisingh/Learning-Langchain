# PyPDF Loader is a document loader in LangChain used to load content from PDF files and covert each page into a Document object
# [
#   Document(page_content= "Text from page 1", meta_data = {"page" : 0, "source": " election.pdf"}),
#   Document(page_content= "Text from page 2", meta_data = {"page" : 1, "source": " election.pdf"}),
# ]

## Limitations
# It is used with PyPDF library inder the hood -- not great with scanned PDFs or complex layouts.

## Some other PDF Loaders 
# For PDFs with tables -> PDFlumberLoader
# Scanned /image PDFs -> UnstructuredPDFLoader or AmazonTextractPDFLoader
# Need layout and image data -> PyMuPDFLoader
# Want best structured extraction -> UnstructuredPDFLoader

from langchain_community.document_loaders import PyPDFLoader 
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

loader = PyPDFLoader("Loader/yolopaper.pdf")
docs = loader.load()

print(docs)
print(type(docs)) # List
print(type(docs[0])) # Document Object
print(len(docs))
print(docs[0].metadata)

# chain =  prompt1 | model1 | parser

# print(chain.invoke({"text": docs}))