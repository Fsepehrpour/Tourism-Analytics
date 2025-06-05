import pandas as pd

df = pd.read_csv('../data/tripadvisor_hotel_reviews.csv')

# Sntiment Classification: Convert ratings into sentiment label
# 1–2 → negative
# 3 → neutral (or drop it for binary classification)
# 4–5 → positive

def map_sentiment(rating):
    if rating <= 2:
        return 'negative'
    elif rating == 3:
        return 'neutral'
    else:
        return 'positive'


df['Sentiment'] = df['Rating'].apply(map_sentiment)

# Drop neutral for binary classification
df = df[df['Sentiment'] != 'neutral']

# Basic Text Cleaning
df['Cleaned_Review'] = df['Review'].str.lower().str.strip()

# Save cleaned file
df[['Cleadned_Review', 'Sentiment']].to_csv('cleaned_hote_review.csv', index=False)