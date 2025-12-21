import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax

nltk.download("punkt")
nltk.download("vader_lexicon")

sia = SentimentIntensityAnalyzer()

MODEL = "cardiffnlp/twitter-roberta-base-sentiment"
tokenizer = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForSequenceClassification.from_pretrained(MODEL)

def vader_scores(text):
    s = sia.polarity_scores(text)
    return {
        "pos": s["pos"],
        "neu": s["neu"],
        "neg": s["neg"],
        "compound": s["compound"]
    }

def roberta_scores(text):
    encoded = tokenizer(text, return_tensors="pt", truncation=True)
    output = model(**encoded)
    scores = softmax(output[0][0].detach().numpy())
    return {
        "neg": scores[0],
        "neu": scores[1],
        "pos": scores[2]
    }

def label_from_scores(pos, neu, neg):
    if pos > neg and pos > neu:
        return "Positive"
    if neg > pos and neg > neu:
        return "Negative"
    return "Neutral"

def emoji_from_label(label):
    return {
        "Positive": "😊",
        "Negative": "😠",
        "Neutral": "😐"
    }[label]

def final_sentiment(vader_label, roberta_label, roberta):
    if vader_label == roberta_label:
        return vader_label

    if roberta_label == "Negative" and roberta["neg"] > 0.6:
        return "Negative"

    if roberta_label == "Positive" and roberta["pos"] > 0.6:
        return "Positive"

    return "Neutral"

def analyze(text):
    vader = vader_scores(text)
    roberta = roberta_scores(text)

    vader_label = label_from_scores(
        vader["pos"], vader["neu"], vader["neg"]
    )

    roberta_label = label_from_scores(
        roberta["pos"], roberta["neu"], roberta["neg"]
    )

    final_label = final_sentiment(
        vader_label, roberta_label, roberta
    )

    return {
        "vader": vader,
        "roberta": roberta,
        "vader_label": vader_label,
        "roberta_label": roberta_label,
        "final_label": final_label,
        "emoji": emoji_from_label(final_label)
    }
