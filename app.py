import streamlit as st
from model import predict

st.title("Sentiment Analysis (TF-IDF + ML)")

text = st.text_area("Enter your text")

if st.button("Analyze") and text.strip():
    result = predict(text)

    st.subheader("Result")

    if result == "positive":
        st.success("Positive 😊")
    elif result == "negative":
        st.error("Negative 😠")
    else:
        st.info("Neutral 😐")
