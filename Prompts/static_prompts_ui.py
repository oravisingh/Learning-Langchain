from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openrouter import ChatOpenRouter
import streamlit as st

load_dotenv()

model = ChatOpenRouter(
    model= "nvidia/nemotron-3.5-lightning:free",
    temperature=0.7,
)

st.set_page_config(page_title="Research Tool", page_icon="📚")
st.header("Research Tool")



prompt = st.text_input("Enter your research prompt here:")

if not prompt.strip():
    st.warning("Please enter a research prompt before generating the response.")
    st.stop()

with st.spinner("Generating result..."):
    if st.button("Summarize"):
        result = model.invoke(prompt)
        st.write(result.content)


