import streamlit as st
from model import analyze

st.set_page_config(page_title="Sentiment Analysis System", page_icon="💬")

st.title("💬 Sentiment Analysis System")

st.write("Enter any sentence and the system will analyze its sentiment using VADER and RoBERTa models.")

text = st.text_area("Enter your text")

if st.button("Analyze") and text.strip():

    result = analyze(text)

    st.subheader("Final Result")
    st.markdown(f"## {result['final_label']} {result['emoji']}")

    st.subheader("Model Breakdown")

    st.write(f"VADER → {result['vader_label']}")
    st.progress(int(result["vader"]["pos"] * 100))

    st.write(f"RoBERTa → {result['roberta_label']}")
    st.progress(int(result["roberta"]["pos"] * 100))