# 😊 Sentiment Analysis System (VADER + RoBERTa)

A **hybrid sentiment analysis system** built using **NLTK (VADER)** and **Hugging Face RoBERTa**, combined with a **Streamlit web interface**.
The system analyzes user text and predicts **Positive, Negative, or Neutral** sentiment with an emoji-based output.

---

## 🚀 Live Demo

🔗 **Try the App:**
https://sentiment-analysis-anshul-rajpoot.streamlit.app/

---

## 📸 Screenshot

<img width="959" height="786" alt="Sentiment Analysis App Screenshot" src="https://github.com/user-attachments/assets/d5b09f38-1714-4bd1-a306-abbc1561b3ca" />

---

## 🚀 Project Overview

This project performs sentiment analysis by **combining lexicon-based and transformer-based models** to improve reliability and accuracy.

The system integrates two approaches:

* **VADER** → Fast rule-based sentiment scoring
* **RoBERTa (Twitter Sentiment Model)** → Deep learning model for contextual understanding

A **custom decision logic layer** combines predictions from both models to generate a final sentiment label.

---

## 🧠 How It Works

1. User enters text in the **Streamlit web application**
2. Text is analyzed using:

   * **VADER SentimentIntensityAnalyzer**
   * **RoBERTa Transformer model**
3. Both models generate sentiment probability scores
4. A rule-based fusion system determines the final sentiment
5. Result is displayed with **emoji and confidence bars**

---

## 📂 Project Structure

```
Sentiment-Analysis/
│
├── app.py             # Streamlit web interface
├── model.py           # Sentiment analysis logic
├── requirements.txt   # Python dependencies
├── runtime.txt        # Python version for deployment
└── README.md
```

---

## 🛠 Technologies Used

* **Python**
* **NLTK (VADER)**
* **Hugging Face Transformers**
* **RoBERTa (twitter-roberta-base-sentiment)**
* **Streamlit**
* **SciPy**

---

## 📌 Models Used

### ✔ VADER (Lexicon-Based)

* Rule-based sentiment analysis model
* Designed for **social media text**
* Returns polarity scores:

```
positive
neutral
negative
compound
```

---

### ✔ RoBERTa (Transformer-Based)

* Pretrained **Twitter sentiment transformer**
* Captures **context, tone, and sarcasm**
* Outputs probability scores for:

```
Positive
Neutral
Negative
```

---

## 🔍 Sentiment Fusion Logic

Final sentiment is determined using the following rules:

* If **VADER and RoBERTa agree** → return that sentiment
* If **RoBERTa confidence > 0.6** → prioritize RoBERTa
* Otherwise → return **Neutral**

This hybrid approach balances:

* ⚡ **Speed (VADER)**
* 🧠 **Contextual understanding (RoBERTa)**

---

## 👨‍💻 Author

**Anshul Rajpoot**
ECE Undergraduate | NLP & Machine Learning Enthusiast

🔗 GitHub
https://github.com/Anshul-Rajpoot

---

⭐ If you like this project, consider **starring the repository**!
