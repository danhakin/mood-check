import streamlit as st
from transformers import pipeline

sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")

st.write("Sentiment Analysis App")

st.text_input("Enter your text:", key="text")

if (st.session_state.text != ""):
    result = sentiment_pipeline(st.session_state.text)
    st.write(result)