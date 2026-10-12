import os

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate,load_prompt
from langchain_openrouter import ChatOpenRouter
import streamlit as st

load_dotenv()

st.set_page_config(page_title="Research Tool", page_icon="📚")
st.header("Research Tool")

paper_title = st.text_input("Enter the paper title")
style = st.selectbox("Select the style", ["Summary", "Detailed Description", "Key-Points"])
length = st.selectbox("Select the desired length", ["short", "medium", "long"])


if not paper_title.strip():
    st.warning("Please enter a paper title before generating the response.")
    st.stop()

if not style:
    st.warning("Please select a style before generating the response.")
    st.stop()

if not length:
    st.warning("Please select a length before generating the response.")
    st.stop()


model = ChatOpenRouter(
    model="nvidia/nemotron-3.5-lightning:free",
    temperature=0.7,
)

template = load_prompt("Prompts/prompt_generator.json")


# We could also use f string instead of PromptTemplate, but using PromptTemplate enables: 1. Default Validation 2. Reusable 3. LangChain Ecosysetm and 4. More Structured Approach and allows for better management of input variables.

with st.spinner("Generating result..."):
    if st.button("Generate"):
        result = model.invoke(prompt)
        st.write(result.content)

