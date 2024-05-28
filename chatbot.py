import json
import time

import streamlit as st
from streamlit_lottie import st_lottie
from transformers import pipeline


def app():
    st.title("My Chatbot 📝")
    st.write("This model can generate text based on your input.")

    def get(path: str):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    path = get("./chatbot.json")
    st_lottie(
        path,
        speed=1,
        width=300,
        height=300,
        key="initial",
    )

    generator = pipeline(
        task="text-generation", model="mistralai/Mistral-7B-Instruct-v0.2"
    )
    text = st.text_area("Enter the  text")
    if st.button("Submit"):
        with st.spinner("Wait for it..."):
            time.sleep(5)
            st.success("Done!")
        generated_text = generator(text)
        st.write(generated_text[0]["generated_text"])

