from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
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

loader = DirectoryLoader(
    path = "Loader",
    glob = "*.pdf", # For different situations -> "**/*.txt", "data/*.csv", e.t.c.
    loader_cls = PyPDFLoader
)

# docs = loader.load() 
docs = loader.lazy_load()

# load() -> Eager loading loads all the things available all at once but when files are too much it take more time 
# lazy_load() -. Lazy Loading can also be used when you have very large number of files, you want to stream the process
# so then documents are not loaded at once instead they are fetched once at a time
# It returns a Generatotr of Document objects instead a List of the same


# print(docs[27])
# print(type(docs)) # List
# print(type(docs[0])) # Document Object
# print(len(docs))
# print(docs[0].metadata)

# chain =  prompt1 | model1 | parser

# print(chain.invoke({"text": docs}))

for files in docs:
    print(files.metadata)