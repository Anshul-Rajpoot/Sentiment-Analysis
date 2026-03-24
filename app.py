import nltk
import string
import joblib

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Download resources
nltk.download("stopwords")
nltk.download("wordnet")

# Initialize tools
stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

# Preprocessing function
def preprocess(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))

    words = text.split()
    words = [w for w in words if w not in stop_words]
    words = [lemmatizer.lemmatize(w) for w in words]

    return " ".join(words)

# Training function
def train_model():
    data = {
        "text": [
            "I love this product",
            "This is amazing",
            "Very bad experience",
            "I hate it",
            "Not good",
            "Absolutely fantastic",
            "Worst purchase ever",
            "Really happy with this",
            "Terrible quality",
            "Very satisfied"
        ],
        "label": [
            "positive", "positive", "negative", "negative", "negative",
            "positive", "negative", "positive", "negative", "positive"
        ]
    }

    texts = [preprocess(t) for t in data["text"]]
    labels = data["label"]

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(texts)

    model = LogisticRegression()
    model.fit(X, labels)

    # Save
    joblib.dump(model, "model.pkl")
    joblib.dump(vectorizer, "vectorizer.pkl")

    return model, vectorizer

# Load or train
def load_model():
    try:
        model = joblib.load("model.pkl")
        vectorizer = joblib.load("vectorizer.pkl")
    except:
        model, vectorizer = train_model()

    return model, vectorizer

# Prediction function
def predict(text):
    model, vectorizer = load_model()

    clean_text = preprocess(text)
    vector = vectorizer.transform([clean_text])

    prediction = model.predict(vector)[0]

    return prediction
