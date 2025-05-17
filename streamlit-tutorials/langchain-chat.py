import os
import streamlit as st
from langchain_openai.chat_models import ChatOpenAI


st.title("Quickstart App")


def generate_response(input_text):
    model = ChatOpenAI(temperature=0.7)
    st.info(model.invoke(input_text))

with st.form("my_form"):
    text = st.text_area(
        "Enter text:",
        "What are the three key pieces of advice for learning how to code?",
    )
    submitted = st.form_submit_button("Submit")
    if submitted:
        generate_response(text)
