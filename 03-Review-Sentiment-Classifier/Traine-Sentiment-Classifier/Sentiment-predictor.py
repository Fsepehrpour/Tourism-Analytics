import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

# load and clean data
@st.cache_data
def load_data():
    df = pd.read_csv('./cleaned_hotel_reviews.csv')
    return df

# Train model with class_weight and stratification
@st.cache_resource
def train_model(df):
    from sklearn.model_selection import train_test_split
    X = df['Cleaned_Review']
    y = df['Sentiment']
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, stratify=y, random_state=42
    )

    vectorizer = TfidfVectorizer(max_features=5000)
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)
    model = LogisticRegression(class_weight='balanced')
    model.fit(X_train_vec, y_train)
    return model, vectorizer, X_test_vec, y_test

# Predict Sentiment
def predict_sentiment(text, model, vectorizer):
    vec = vectorizer.transform([text])
    return model.predict(vec)[0]


# Plot confusion matrix
def plot_confusion_matrix(y_true, y_pred, title="Confusion Matrix"):
    cm = confusion_matrix(y_true, y_pred, labels=["positive", "negative"])
    fig, ax = plt.subplots()
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
                xticklabels=["positive", "negative"],
                yticklabels=["positive", "negative"], ax=ax)
    ax.set_xlabel("Predicted")
    ax.set_ylabel("Actual")
    ax.set_title(title)
    st.pyplot(fig)

# Streamlit UI
st.set_page_config(page_title="Hotel Review Sentiment Classifier", layout="wide")
st.title("Hotel Review Sentiment Classifier")

df = load_data()
model, vectorizer, X_test_vec, y_test = train_model(df)

st.markdown("### Enter a hotel review to analyze its sentiment")
user_input = st.text_area("Type your review here:", "")

if user_input:
    prediction = predict_sentiment(user_input, model, vectorizer)
    st.success(f"✅ Predicted Sentiment: **{prediction.capitalize()}**")

# Show evaluation section
st.markdown("###  Model Performance on Sample Data")
if st.checkbox("Show evaluation"):
    from sklearn.metrics import classification_report

    y_pred = model.predict(X_test_vec)
    plot_confusion_matrix(y_test, y_pred, "Logistic Regression Confusion Matrix")
    st.text("Classification Report:")
    st.text(classification_report(y_test, y_pred))


