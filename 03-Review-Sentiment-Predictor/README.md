# Hotel Review Sentiment Classifier

This project builds a machine learning model to classify hotel reviews from TripAdvisor as **positive** or **negative** using text sentiment analysis. It includes both training scripts and an interactive Streamlit dashboard for live predictions.

---

## Project Structure

```plaintext
03-REVIEW-SENTIMENT-Predictor/
│
├── data/                             # Raw review dataset
│   └── tripadvisor_hotel_reviews.csv
│
├── Review-Sentiment-Classifier/
│   ├── classifier.py
│   ├── classifier.ipynb
│   ├── cleaned_hotel_reviews.csv
│   └── README.md
│
│
├── Review-Sentiment-Predictor/      # Model training and evaluation
│   ├── cleaned_hotel_reviews.csv
│   ├── model-training.ipynb
│   ├── model-training.py
│   └── Predictor-dashboard.py       # Streamlit app
```

## Objectives
- Automatically label hotel reviews as positive or negative based on textual content
- Train and evaluate multiple models (Logistic Regression, Naive Bayes)
- Visualize performance using confusion matrices
- Deploy a simple, user-friendly Streamlit dashboard for live prediction

## Workflow
1. **Data Cleaning**
- Loaded and preprocessed raw data
- Converted star ratings to sentiment labels:
    - 1–2 → negative
    - 3 → neutral (excluded)
    - 4–5 → positive
- Cleaned text (lowercasing, trimming)
- Saved processed file as cleaned_hotel_reviews.csv

2. **Model Training**
- Used **TF-IDF** to vectorize review text
- Trained two classifiers:
    - LogisticRegression(class_weight='balanced')
    - MultinomialNB()
- Evaluated both models using precision, recall, f1-score, and confusion matrix

3. **Streamlit App**
- Interactive dashboard (Predictor-dashboard.py)
- User inputs a hotel review → model predicts sentiment
- Option to display classification report and confusion matrix


## Model Results

| Metric          | Logistic Regression | Naive Bayes |
| --------------- | ------------------- | ----------- |
| Accuracy        | 95.1%               | 92.0%       |
| Positive Recall | 95.5%               | 99.4%       |
| Negative Recall | **93.3%**           | 57.5%       |

_Logistic Regression offers more balanced performance and stronger detection of negative reviews._

### How to Run the App
```
#Install requirements
pip install streamlit pandas scikit-learn matplotlib seaborn

# Run Streamlit app
streamlit run Predictor-dashboard.py
```

### Author
Fatemeh Sepehrpour

[LinkedIn](www.linkedin.com/in/fatemeh-sepehrpour-012982ba)



