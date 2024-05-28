import json
import time

import streamlit as st
from streamlit_lottie import st_lottie
from transformers import pipeline


def app():
    st.title("Question Answering Model 🤖")
    st.write("This model can answer your questions based on the context you provide.")

    def get(path: str):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    path = get("./qa.json")

    st_lottie(
        path,
        speed=1,
        width=300,
        height=300,
        key="initial",
    )

    nlp = pipeline(task="question-answering", model="deepset/roberta-base-squad2")

    context = st.text_area("Enter the paragraph")
    question = st.text_input("Enter the question")
    if st.button("Submit"):
        with st.spinner("Wait for it..."):
            time.sleep(5)
            st.success("Done!")
        answer = nlp(question=question, context=context)
        st.write("Answer: {}".format(answer["answer"]))

