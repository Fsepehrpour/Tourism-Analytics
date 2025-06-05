import pandas as pd

df = pd.read_csv('./cleaned_hotel_reviews.csv')

# Split Feautures and Labels
X = df['Cleaned_Review'] # text
y = df['Sentiment'] # label: positive or negative

# Split data with into train and test stratification to preserve class balance
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

# Vectorize Text with TF-IDF
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(max_features=5000)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train the models

## Logistic Regression (with class_weight to handle imbalance)
from sklearn.linear_model import LogisticRegression

lr_model = LogisticRegression(class_weight='balanced')
lr_model.fit(X_train_vec, y_train)
lr_preds = lr_model.predict(X_test_vec)


## Naive Bayes
from sklearn.naive_bayes import MultinomialNB

nb_model = MultinomialNB()
nb_model.fit(X_train_vec, y_train)
nb_preds = nb_model.predict(X_test_vec)

# Evaluate the models
from sklearn.metrics import classification_report

print("Logistic Regression Report:")
print(classification_report(y_test, lr_preds))



print("Naive Bayes Report:")
print(classification_report(y_test, nb_preds))


# Visualize Confusion Matrices

from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns


# Confusion Matrices
lr_cm = confusion_matrix(y_test, lr_preds, labels=["positive", "negative"])
nb_cm = confusion_matrix(y_test, nb_preds, labels=["positive", "negative"])


# Plot Matrices
fig, axes = plt.subplots(1,2, figsize=(12,5))

sns.heatmap(lr_cm, annot=True, fmt='d', cmap='Blues', ax=axes[0],
            xticklabels=['positive', 'negative'],
            yticklabels=['positive', 'negative'])
axes[0].set_title('Logistic Regression')

sns.heatmap(nb_cm, annot=True, fmt='d', cmap='Greens', ax=axes[1],
            xticklabels=['positive', 'negative'],
            yticklabels=['positive', 'negative'])
axes[1].set_title('Naive Bayes')

plt.tight_layout()
plt.show()

