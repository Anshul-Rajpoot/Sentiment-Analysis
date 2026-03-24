import streamlit as st
from model import predict

# Sidebar developer card
st.sidebar.markdown(
    """
    <div style="
        background-color:#1f2937;
        padding:20px;
        border-radius:12px;
        color:white;
        text-align:left;
        box-shadow:0px 4px 15px rgba(0,0,0,0.3);
    ">
        <h3 style="margin-bottom:10px;">👨‍💻 Developer</h3>
        <p><b>Name:</b> Anshul Rajpoot</p>
        <p><b>Scholar Number:</b> 2311401168</p>
        <p><b>College:</b> MANIT Bhopal</p>
        <p><b>Branch:</b> Electronics & Communication</p>
        <p><b>Project:</b> Movie Recommendation System</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.title("Sentiment Analysis System")

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
