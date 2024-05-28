import json
import time
import streamlit as st
from streamlit_lottie import st_lottie
from transformers import pipeline


def app():
    st.title("Text Summarization 📚")
    st.write("This model can summarize the text based on the input you provide.")

    def get(path: str):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    path = get("./summ.json")
    st_lottie(
        path,
        speed=1,
        width=400,
        height=400,
        key="initial",
    )
    suumm = pipeline(task="summarization", model="facebook/bart-large-cnn")

    text = st.text_area("Enter the text")
    if st.button("Summarize"):
        with st.spinner("Wait for it..."):
            time.sleep(5)
            st.success("Done!")
        summary_text = suumm(text)
        st.write(summary_text[0]["summary_text"])
