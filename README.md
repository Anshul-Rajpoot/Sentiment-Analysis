# 😊 Sentiment Analysis System (Hybrid + ML Models)

A **comprehensive sentiment analysis system** combining both:

- 🔹 **Classical Machine Learning (TF-IDF + Logistic Regression)**
- 🔹 **Hybrid NLP Models (VADER + RoBERTa)**

Built with a **Streamlit web interface**, the system classifies text into **Positive, Negative, or Neutral** sentiment with emoji-based output.

---

## 🚀 Live Demo

🔗 **Try the App:**
https://sentiment-analysis-anshul-rajpoot.streamlit.app/

---


## 🚀 Project Overview

This project demonstrates **multiple approaches to sentiment analysis**:

### 🔹 1. Classical ML Pipeline
- Text preprocessing using **NLTK**
- Feature extraction using **TF-IDF**
- Classification using **Logistic Regression**
- Evaluation using **Confusion Matrix, Precision, Recall, and F1-score**

### 🔹 2. Hybrid Deep Learning System
- **VADER** → Rule-based sentiment scoring
- **RoBERTa** → Transformer-based contextual understanding
- **Custom decision logic** to combine both outputs

This makes the project a **complete end-to-end NLP system** covering both **traditional ML and modern deep learning approaches**.

---

## 🧠 How It Works

### 🔹 ML Pipeline (TF-IDF + Logistic Regression)

1. Input text is preprocessed:
   - Tokenization
   - Stop-word removal
   - Lemmatization
2. Text is converted into numerical vectors using **TF-IDF**
3. Logistic Regression model predicts sentiment
4. Model performance is evaluated using standard metrics

---

### 🔹 Hybrid Model (VADER + RoBERTa)

1. User enters text in the **Streamlit app**
2. Text is analyzed using:
   - **VADER (NLTK)**
   - **RoBERTa (Hugging Face Transformer)**
3. Both models generate sentiment scores
4. A **fusion logic layer** determines final sentiment
5. Output displayed with emoji and confidence bars

---

## 📂 Project Structure
Sentiment-Analysis/
│
├── app.py # Streamlit web interface
├── model.py # Hybrid sentiment logic (VADER + RoBERTa)
├── train_model.py # ML model training (TF-IDF + Logistic Regression)
├── predict.py # ML model prediction
├── model.pkl # Trained ML model
├── vectorizer.pkl # TF-IDF vectorizer
├── requirements.txt # Dependencies
├── runtime.txt # Python version
└── README.md
