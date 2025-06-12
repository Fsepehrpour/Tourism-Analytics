# Interactive Destination Recommender

A data-driven application that helps travelers find the perfect destination based on their budget, travel season, and interests. Built using **Python**, **Pandas**, and **Streamlit**, this project demonstrates skills in data cleaning, enrichment, rule-based filtering, and user-centric UI design.

---

## Project Overview

This project recommends travel destinations by analyzing historical trip data and applying user-defined filters. The system uses a cleaned and enriched dataset with over 200 entries, including synthetic traveler data for diversity.

**Key Features:**
- Filter by **budget**, **season**, and **interest category**
- Displays average total travel cost for each destination
- Simple, interactive web interface powered by Streamlit

---

## Project Structure
````
Interactive-Destination-Recommender/
│
├── cleaned_travel_dataset.csv # Cleaned and enriched dataset
├── app.py # Streamlit app for user interaction
│
├── data_exploration_cleaning.ipynb
├── README.md # Project documentation
└── requirements.txt # Python dependencies
````

---

## Tools & Technologies

- **Python** (Data manipulation and logic)
- **Pandas** (Cleaning, filtering, transformation)
- **Streamlit** (Web-based UI)
- **Git/GitHub** (Version control)
- **Data Enrichment**:
  - Budget simulation
  - Interest category tagging
  - Seasonal classification
  - Synthetic data generation (Faker)

---

## How to Run the App

1. Clone the repository:

```
git clone https://github.com/Fsepehrpour/Tourism-Analytics/05-Interactive-Destination-Recommender
cd Interactive-Destination-Recommender
```

2. Install independencies

```
pip install -r requiremets.txt
```

3. Launch the app
```
streamlit run app.py
```

#### Sample User Filters
- Budget: up to €1500
- Preferred season: Summer
- Interest: Beach

The app will return a ranked list of affordable destinations that match your travel style.


## Future Improvements
- Integrate destination images and descriptions
- Use ML models (e.g., clustering or collaborative filtering) for personalized recommendations
- Add maps and visualizations
- Enable user feedback and data logging

## Author
Fatemeh Sepehrpour
Tourism & Data Analytics Enthusiast


