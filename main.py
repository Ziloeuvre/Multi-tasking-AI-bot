import streamlit as st
from streamlit_option_menu import option_menu

import chatbot
import Home
import qa
import senti
import summ
import tran

st.set_page_config(
    page_title="Models",
    page_icon="🧊",
)


class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({"title": title, "function": func})

    def run():
        # app = st.sidebar(
        with st.sidebar:
            app = option_menu(
                menu_title="MODELS ",
                options=[
                    "Home",
                    "Q&A",
                    "Translator",
                    "Summarization",
                    "Generation",
                    "Sentiment Analysis",
                ],
                icons=[
                    "circle-fill",
                    "circle-fill",
                    "circle-fill",
                    "circle-fill",
                    "circle-fill",
                    "circle-fill",
                ],
                menu_icon="chat-text-fill",
                default_index=0,
                styles={
                    "container": {
                        "padding": "5!important",
                        "background-color": "light-black",
                    },
                    "icon": {"color": "white", "font-size": "23px"},
                    "nav-link": {
                        "color": "white",
                        "font-size": "20px",
                        "text-align": "left",
                        "margin": "0px",
                        "--hover-color": "purple",
                    },
                    "nav-link-selected": {"background-color": "#02ab21"},
                },
            )

        if app == "Home":
            Home.app()
        if app == "Q&A":
            qa.app()
        if app == "Translator":
            tran.app()
        if app == "Summarization":
            summ.app()
        if app == "Generation":
            chatbot.app()
        if app == "Sentiment Analysis":
            senti.app()

    run()
