# 🏨 Hotel Performance Dashboard

This project explores hotel reservation data through interactive visualizations using **Streamlit** and **Tableau Public**. The goal is to uncover key insights about customer behavior, booking trends, and cancellation patterns in a clear and engaging way.

## 🔍 Project Summary

Using a dataset of hotel reservations, this dashboard provides:

- **Key Performance Indicators (KPIs)** like total bookings, cancellation rate, average room price, lead time, and guest repetition rate.
- **Interactive charts** to explore:
  - Booking status (Confirmed vs. Canceled)
  - Cancellation rate by market segment
  - Monthly booking trends
  - Room price distribution per market segment

The project is built with **Python**, **Pandas**, **Plotly**, and **Streamlit** for the interactive dashboard, and **Tableau Public** for a polished visual storytelling experience.

---

## 📊 Streamlit Dashboard

### ▶️ How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/Fsepehrpour/Tourism-Analytics/tree/ed329978e95adf9d047706af46e24360c2f3f74d/06-Hotel-Reservation-Dashboard
   ```
   cd Hotel-Reservation-Dashboard

2. Install dependencies
```
pip install -r requirements.txt
```

3. Run the Streamlit app:
```
streamlit run src/streamlit-dashboard.py
```

## Project Structure

Hotel-Performance-Dashboard/
│
├── data/
│   └── Hotel-Reservations.csv           # Raw dataset
│
├── src/
│   ├── .streamlit/
│   │   └── config.toml                  # Streamlit theme config
│   └── streamlit-dashboard.py          # Streamlit app code
│
├── Tableau-dashboard.png                # Screenshot of Tableau dashboard
├── README.md                            # Project overview
├── requirements.txt                     # Python dependencies



## 📈 Tableau Public Dashboard
🔗 [View on Tableau Public](https://public.tableau.com/views/FinalProjectBIAnalysis/Dashboard1?:language=en-GB&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)


## ✨ Skills Demonstrated
- Data Cleaning & Aggregation (Pandas)
- Interactive Visualization (Plotly, Streamlit)
- UI Design in Data Dashboards
- Comparative Analysis in Visualization Tools (Streamlit vs. Tableau)

##Dataset Source
This dataset was sourced from Kaggle and contains booking information such as price, date, cancellation status, and customer type.
🔗 [Hotel Reservations Dataset on Kaggle](https://www.kaggle.com/datasets/ahsan81/hotel-reservations-classification-dataset/data)

### Author
Fatemeh Sepehrpour
Feel free to connect on [LinkedIn](www.linkedin.com/in/fatemeh-sepehrpour-012982ba) or explore more on [GitHub](https://github.com/Fsepehrpour)



