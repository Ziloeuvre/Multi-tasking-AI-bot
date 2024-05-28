import json
import time

import streamlit as st
from streamlit_lottie import st_lottie
from transformers import pipeline


def app():
    st.title("Text Translation 🌍")
    st.write("This model can translate text from English to German.")

    def get(path: str):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    path = get("./tran.json")
    st_lottie(
        path,
        speed=1,
        width=400,
        height=400,
        key="initial",
    )

    translator = pipeline(task="translation", model="google-t5/t5-small")
    text_key = "text_input"
    translate_key = "translate_button"

    text = st.text_area("Enter the text.")
    if st.button("Translate", key=translate_key):
        with st.spinner("Wait for it..."):
            time.sleep(10)
            st.success("Done!")
        translated_text = translator(text)
        st.write(translated_text[0]["translation_text"])


# how tranlator model works
