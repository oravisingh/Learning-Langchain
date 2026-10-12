import os

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openrouter import ChatOpenRouter
import streamlit as st

load_dotenv()

st.set_page_config(page_title="Research Tool", page_icon="📚")
st.header("Research Tool")

with st.form("research_tool_form"):
    paper_title = st.text_input("Enter the paper title")
    style = st.selectbox("Select the style", ["Summarize", "Detailed Description", "Key-Points"])
    length = st.selectbox("Select the desired length", ["short", "medium", "long"])
    submitted = st.form_submit_button("Generate")

if not submitted:
    st.info("Enter a paper title and click Generate to create a research summary.")
    st.stop()

if not paper_title.strip():
    st.warning("Please enter a paper title before generating the response.")
    st.stop()


model = ChatOpenRouter(
    model="nvidia/nemotron-3.5-lightning:free",
    temperature=0.7,
)

template = PromptTemplate(
    input_variables=["paper_title", "style", "length"],
    template="""
        You are a research assistant.
        Write a {style} of the paper titled "{paper_title}".
        Keep the response {length} in length.
        Focus on the main ideas, significance, methods, and key takeaways.
        Present it in clear, professional English.
        """,
        )

prompt = template.invoke({
    "paper_title": paper_title,
    "style": style,
    "length": length,
})

with st.spinner("Generating result..."):
    result = model.invoke(prompt)

st.write(result.content)
