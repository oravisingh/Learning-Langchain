import os

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
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

template = PromptTemplate(
    input_variables=["paper_title", "style", "length"],
    template="""
        You are a research assistant.
        Write a {style} of the paper titled "{paper_title}".
        Keep the response {length} in length.
        Focus on the main ideas, significance, methods, and key takeaways.
        Present it in clear, professional English.
        1.Mathemaitcal Formula:
            -Use the mathematical formula(if any) as well to explain in a simple manner.
        2.Analogy:
            -Use analogy to explain the concept in a simple manner. 
        """,
        )

prompt = template.invoke({
    "paper_title": paper_title,
    "style": style,
    "length": length,
})

with st.spinner("Generating result..."):
    if st.button("Generate"):
        result = model.invoke(prompt)
        st.write(result.content)

