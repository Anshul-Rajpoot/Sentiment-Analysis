import streamlit as st
from model import analyze

st.title("Sentiment Analysis System")

text = st.text_area("Enter your text")

if st.button("Analyze") and text.strip():
    result = analyze(text)

    st.subheader("Final Result")
    st.markdown(f"## {result['final_label']} {result['emoji']}")

    st.subheader("Model Breakdown")

    st.write(f"VADER → {result['vader_label']}")
    st.progress(result["vader"]["pos"])

    st.write(f"RoBERTa → {result['roberta_label']}")
    st.progress(int(result["roberta"]["pos"] * 100))
