import streamlit as st
from model import analyze

st.set_page_config(page_title="Sentiment Analysis System", page_icon="💬")

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
        <p><b>Project:</b> Sentiment Analysis System</p>
    </div>
    """,
    unsafe_allow_html=True
)

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
