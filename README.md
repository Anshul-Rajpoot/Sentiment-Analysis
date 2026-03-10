# 😊 Sentiment Analysis System (VADER + RoBERTa)

A **hybrid sentiment analysis system** built using **NLTK (VADER)** and **Hugging Face RoBERTa**, combined with a **Streamlit web interface**.  
The system analyzes user text and predicts **Positive, Negative, or Neutral** sentiment with an emoji-based output.

## 🚀Screen Shot
<img width="959" height="786" alt="image" src="https://github.com/user-attachments/assets/d5b09f38-1714-4bd1-a306-abbc1561b3ca" />


---

## 🚀 Project Overview

This project performs sentiment analysis by **combining lexicon-based and transformer-based models**:

- **VADER** → Fast, rule-based sentiment scoring
- **RoBERTa (Twitter Sentiment Model)** → Deep learning-based contextual understanding

A final sentiment label is decided using **custom decision logic** to improve reliability.

---

## 🧠 How It Works

1. User enters text in the Streamlit app
2. Text is analyzed using:
   - **VADER SentimentIntensityAnalyzer**
   - **RoBERTa transformer model**
3. Both models generate sentiment scores
4. A final sentiment is chosen using rule-based fusion
5. Result is displayed with **emoji and confidence bars**

---

## 📂 Project Structure

Sentiment-Analysis/
│
├── model.py # Sentiment analysis logic
├── app.py # Streamlit application
├── requirements.txt # Dependencies
└── README.md


---

## 🛠 Technologies Used

- Python
- NLTK (VADER)
- Hugging Face Transformers
- RoBERTa (twitter-roberta-base-sentiment)
- Streamlit
- SciPy

---

## 📌 Models Used

### ✔ VADER (Lexicon-Based)
- Rule-based sentiment analysis
- Returns polarity scores: `positive`, `neutral`, `negative`, `compound`

### ✔ RoBERTa (Transformer-Based)
- Pretrained Twitter sentiment model
- Captures contextual meaning and sarcasm
- Outputs probability scores for each sentiment

---

## 🔍 Sentiment Fusion Logic

Final sentiment is decided as follows:

- If **VADER & RoBERTa agree** → return that sentiment
- If RoBERTa confidence > **0.6** → prioritize RoBERTa
- Otherwise → Neutral

This approach balances **speed + accuracy**.

---

👨‍💻 Author

Anshul Rajpoot
ECE Undergraduate | NLP & Machine Learning Enthusiast
🔗 GitHub: https://github.com/Anshul-Rajpoot



