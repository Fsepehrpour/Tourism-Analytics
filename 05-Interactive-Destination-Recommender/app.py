import streamlit as st
import pandas as pd

# Load cleaned data
df = pd.read_csv("./cleaned_travel_dataset.csv")

# Sidebar inputs
st.sidebar.title("Travel Preferences")

budget = st.sidebar.slider("Maximum Budget in €", 100, 500, 1500, step=100)
season = st.sidebar.selectbox("Preferred Season", df['season'].dropna().unique())
interest = st.sidebar.selectbox("Interest Category", df['interest_category'].dropna().unique())

# Title
st.title("Destination Recommender")

# Filter Logic
filtered_df = df[
    (df['total_cost'] <= budget) &
    (df['season'] == season) &
    (df['interest_category'] == interest)
]

# Group by destination to show distinct result
results = filtered_df.groupby('destination').agg({
    'total_cost':'mean',
    'season' : 'first',
    'interest_category': 'first'
}).sort_values(by='total_cost').reset_index()

# Output 
if not results.empty:
    st.success(f"Found{len(results)} destination(s) matching your preferences:")
    st.dataframe(results.rename(columns={
        'destination': 'Destination',
        'total_cost': 'Avg Total Cost in €',
        'season': 'Season',
        'interest_category': 'Interest'
    }))
else:
    st.warning("No destination match your preferences. Try adjusting your filters.")
