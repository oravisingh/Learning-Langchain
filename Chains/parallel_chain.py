#From a single document We will be generating a notes and a quiz parallely
# Dont't be frightened the extra stuff if just for fun to generate the esponse in a PDF actually

from pathlib import Path
from xml.sax.saxutils import escape

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openrouter import ChatOpenRouter
from langchain_core.runnables import RunnableParallel

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer

load_dotenv()

model = ChatOpenRouter(
    model="nvidia/nemotron-3.5-super-vl:free",
    temperature=0.7,
    # max_tokens=500,
)

# Defining Parsers
prompt1 = PromptTemplate(
    template = "Generate a crisp note from the given {text}",
    input_variables = ["text"]
)

prompt2 = PromptTemplate(
    template = "Generate a 5 question quiz from the given {text}",
    input_variables = ["text"]
)

prompt3 = PromptTemplate(
    template = "Merge both the provided note and quiz into a single document \n notes-> {notes} and quiz -> {quiz}",
    input_variables = ["notes", "quiz"]
)

# Defining Parsers
parser = StrOutputParser()

# Defining Chains
parallel_chain = RunnableParallel({
    "notes": prompt1 | model | parser,
    'quiz': prompt2 | model | parser
})

merge_chain = prompt3 | model | parser

chain = parallel_chain | merge_chain

# The PDF output stuff
def save_result_as_pdf(text: str) -> Path:
    pdf_path = Path(__file__).with_name("parallel_chain_result.pdf")
    document = SimpleDocTemplate(
        str(pdf_path),
        pagesize=letter,
        rightMargin=0.75 * inch,
        leftMargin=0.75 * inch,
        topMargin=0.75 * inch,
        bottomMargin=0.75 * inch,
        title="Generated Notes and Quiz",
    )
    styles = getSampleStyleSheet()
    content = []

    for paragraph in text.split("\n\n"):
        if paragraph.strip():
            content.append(Paragraph(escape(paragraph).replace("\n", "<br/>"), styles["BodyText"]))
            content.append(Spacer(1, 0.15 * inch))

    document.build(content)
    return pdf_path


# Invoking the Chain
input_text = Path(__file__).with_name("middle_east_crisis.txt").read_text(encoding="utf-8")
result = chain.invoke({"text": input_text})

pdf_path = save_result_as_pdf(result)
print(f"PDF saved to: {pdf_path}")
print(result)