import json

import streamlit as st
from streamlit_lottie import st_lottie


def app():
    def get(path: str):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    path = get("./Home.json")

    st_lottie(
        path,
        speed=1,
        width=500,
        height=500,
        key="initial",
    )

    st.title("Welcome to the AI Hub 🤖")
