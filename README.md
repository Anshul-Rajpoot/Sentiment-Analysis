# 😊 Sentiment Analysis System

A **sentiment analysis web application** that classifies text into **Positive, Negative, or Neutral** using a **classical machine learning pipeline**.

Built with an interactive **Streamlit interface** for real-time predictions.

---

## 🚀 Live Demo

🔗 https://sentiment-analysis-anshul-rajpoot.streamlit.app/

---

## ⚡ Key Features

* 🔹 Real-time sentiment prediction
* 🔹 Clean and interactive **Streamlit UI**
* 🔹 Emoji-based output for better user experience
* 🔹 Lightweight and fast ML model
* 🔹 Modular code structure

---

## 🧠 Model Overview

### 🔹 Machine Learning Pipeline

* Text preprocessing using **NLTK**

  * Lowercasing
  * Stop-word removal
  * Lemmatization
* Feature extraction using **TF-IDF**
* Classification using **Logistic Regression**

---

## ⚙️ How It Works

1. User enters text in the web interface
2. Text is preprocessed using NLP techniques
3. TF-IDF converts text into numerical features
4. Logistic Regression predicts sentiment
5. Result is displayed with emoji output

---

## 📂 Project Structure

```
Sentiment-Analysis/
│
├── app.py              # Streamlit UI
├── model.py            # Preprocessing + model logic
├── model.pkl           # Trained model
├── vectorizer.pkl      # TF-IDF vectorizer
├── requirements.txt    # Dependencies
└── README.md
```

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit**
* **NLTK**
* **Scikit-learn**

---

## 📊 Limitations

* Uses a small dataset for training
* Limited accuracy on real-world data
* Does not handle complex context or sarcasm

---

## 🚀 Future Improvements

* Train on larger real-world datasets
* Add deep learning models (BERT / RoBERTa)
* Improve preprocessing (negation, emojis)
* Add confidence score visualization

---

## 👨‍💻 Author

**Anshul Rajpoot**
Electronics & Communication Engineering
MANIT Bhopal

---

## ⭐ Notes

This project demonstrates:

* End-to-end ML pipeline development
* Text preprocessing using NLP techniques
* Deployment of ML applications using Streamlit

---
