import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Download NLTK resources
nltk.download('stopwords')
nltk.download('wordnet')

# -----------------------------
# Text Preprocessing Function
# -----------------------------
def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()

    # Remove punctuation, numbers and special characters
    text = re.sub(r'[^a-zA-Z\s]', '', text)

    # Tokenization
    words = text.split()

    # Remove stopwords and perform lemmatization
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()

    words = [
        lemmatizer.lemmatize(word)
        for word in words
        if word not in stop_words
    ]

    return " ".join(words)


def main():

    print("=" * 65)
    print("      SENTIMENT ANALYSIS USING MACHINE LEARNING")
    print("        Logistic Regression + TF-IDF")
    print("=" * 65)

    # -------------------------------------------------
    # Step 1 : Load Dataset
    # -------------------------------------------------
    print("\n[1] Loading IMDB Dataset...")

    df = pd.read_csv("IMDB Dataset.csv")

    # Convert labels into numbers
    df["sentiment"] = df["sentiment"].map({
        "positive": 1,
        "negative": 0
    })

    # -------------------------------------------------
    # Step 2 : Text Cleaning
    # -------------------------------------------------
    print("[2] Cleaning and Preprocessing Reviews...")

    df["cleaned_review"] = df["review"].apply(preprocess_text)

    # -------------------------------------------------
    # Step 3 : Train-Test Split
    # -------------------------------------------------
    print("[3] Splitting Dataset...")

    X = df["cleaned_review"]
    y = df["sentiment"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.25,
        random_state=42
    )

    # -------------------------------------------------
    # Step 4 : TF-IDF
    # -------------------------------------------------
    print("[4] Extracting TF-IDF Features...")

    vectorizer = TfidfVectorizer()

    X_train_tfidf = vectorizer.fit_transform(X_train)
    X_test_tfidf = vectorizer.transform(X_test)

    # -------------------------------------------------
    # Step 5 : Train Model
    # -------------------------------------------------
    print("[5] Training Logistic Regression Model...")

    model = LogisticRegression(max_iter=1000)

    model.fit(X_train_tfidf, y_train)

    # -------------------------------------------------
    # Step 6 : Evaluation
    # -------------------------------------------------
    print("[6] Evaluating Model...")

    y_pred = model.predict(X_test_tfidf)

    accuracy = accuracy_score(y_test, y_pred)

    print("\n" + "=" * 65)
    print("                 MODEL PERFORMANCE")
    print("=" * 65)

    print(f"\nAccuracy : {accuracy * 100:.2f}%")

    print("\nClassification Report:\n")
    print(classification_report(y_test, y_pred))

    print("Confusion Matrix:\n")
    print(confusion_matrix(y_test, y_pred))

    # -------------------------------------------------
    # Step 7 : Prediction
    # -------------------------------------------------
    print("\n" + "=" * 65)
    print("          SENTIMENT ANALYSIS ON NEW REVIEWS")
    print("=" * 65)

    new_reviews = [
        "I really enjoyed the storyline and the characters.",
        "This was absolutely disgusting and boring."
    ]

    for review in new_reviews:

        print("\nOriginal Review:")
        print(review)

        cleaned_review = preprocess_text(review)

        print("\nCleaned Review:")
        print(cleaned_review)

        review_vector = vectorizer.transform([cleaned_review])

        prediction = model.predict(review_vector)[0]

        confidence = model.predict_proba(review_vector).max()

        sentiment = "Positive 😊" if prediction == 1 else "Negative 😞"

        print(f"\nPrediction Confidence : {confidence:.2f}")
        print(f"Predicted Sentiment   : {sentiment}")

        print("-" * 65)


if __name__ == "__main__":
    main()