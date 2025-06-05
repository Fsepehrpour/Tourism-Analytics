# Customer Review Sentiment Classifier

This project analyzes hotel reviews from TripAdvisor and classifies them as **positive** or **negative** using basic Natural Language Processing (NLP).

## 🗂 Dataset

- Source: [TripAdvisor Hotel Reviews on Kaggle](https://www.kaggle.com/datasets/andrewmvd/trip-advisor-hotel-reviews)
- Total entries: 20,000+
- Each review includes:
  - Free-text review
  - Star rating (1–5)

## Data Cleaning

- Ratings were mapped to sentiment:
  - 1–2 → Negative
  - 4–5 → Positive
  - 3-star reviews were removed for binary classification
- Text was lowercased and stripped of extra spacing

## Tools Used
Python · Pandas · Git · Jupyter

## Next Steps to Take

- Vectorize text using TF-IDF
- Train Logistic Regression and Naive Bayes models
- Evaluate performance (accuracy, confusion matrix)
- Visualize top features and predictions
- Deploy a simple Streamlit app



