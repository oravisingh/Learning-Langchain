### WebBaseLoader is a document Loader in LangChain used to load and extract text content from web pages(URLs).
# It uses BeautifulSoup under the hood to parse HTML and extract visible text.

## When to use
# For blogs, news articles, or public websites wherre the content is primarily text-based and static.

## Limitations
# Doesn't handle Javascript heavy pages well ( use SeleniumURLLoader got that)
# Loads only static content(what's into HTML, not what loads after the page renders)

from langchain_community.document_loaders import PyPDFLoader, WebBaseLoader 
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
    template = "How can the CEC be removed according to {text}",
    input_variables = ["text"]

)

url = "https://en.wikipedia.org/wiki/Election_Commission_of_India"
loader = WebBaseLoader(url) # We can also pass a list of urls
docs = loader.load()

# print(docs)
# print(type(docs)) # List
# print(type(docs[0])) # Document Object
# print(len(docs))
# print(docs[0].metadata)

chain =  prompt1 | model1 | parser

print(chain.invoke({"text": docs}))