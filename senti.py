import json
import time

import streamlit as st
from streamlit_lottie import st_lottie
from transformers import pipeline


def app():
    st.title("Sentiment Analysis Model 😊")
    st.write("This model can analyze your sentiment based on provided context.")

    def get(path: str):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    path = get("./senti.json")

    st_lottie(
        path,
        speed=1,
        width=300,
        height=300,
        key="initial",
    )

class SentimentAnalyzer:
    def __init__(self, pre_trained_model) -> None:
        self.classifier = pipeline("sentiment-analysis", model=pre_trained_model)

    def run(self):
        self._render_input_area()
        self._text_analyzer()

    def _render_input_area(self):
        st.markdown("# Sentiment Analysis App")
        st.write("This app using pretrained DistilBERT model for sentiment analysis")
        self.text_input = st.text_area(
            "Enter text for sentiment",
            placeholder="E.g., I Love Entity!",
            height=180,
            max_chars=500,
        )

    def _text_analyzer(self):
        if st.button("Analyze"):
            if self.text_input.strip() == "":
                st.warning("Please enter some text")
            else:
                result = self.classifier(self.text_input)[0]
                emoji = "😊" if result["label"] == "POSITIVE" else "😔"
                st.success(f"Sentiment: {result['label']} {emoji}")
                st.write(f"Confidence: {(result['score'] * 100):.2f}%")


def main():
    pre_trained_model = "distilbert/distilbert-base-uncased-finetuned-sst-2-english"
    analyzer = SentimentAnalyzer(pre_trained_model)
    analyzer.run()



if __name__ == "__main__":
    main()


    #  nlp = pipeline(
    #     task="sentiment-analysis",
    #     model="distilbert/distilbert-base-uncased-finetuned-sst-2-english",
    # )

    # statement = st.text_input("Enter your statement")
    # if statement.strip() == "":
    #     st.warning("Please enter some text")
    # elif st.button("Analyze"):
    #     with st.spinner("Wait for it..."):
    #         time.sleep(5)
    #         st.success("Done!")
    # else:
    #     result = nlp(statement)[0]
    #     emoji = "😊" if result["label"] == "POSITIVE" else "😔"
    #     st.success(f"Sentiment: {result['label']} {emoji}")
    #     st.write(f"Confidence: {(result['score']*100):.2f}%")