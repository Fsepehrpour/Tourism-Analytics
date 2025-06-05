import os
os.environ["STREAMLIT_THEME"] = "custom"

import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("../data/Hotel-Reservations.csv")


# Page Config

st.set_page_config(
    page_title="Hotel Reservation Dashboard",
    page_icon="🏨",
    layout='wide'
)


# Title
st.markdown("<h1 style= 'text-align: center;' >Hotel Reservation Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<br>",unsafe_allow_html=True)

style = """
<h4 style='
    text-align: center;
    background-color: #fff3cd;
    padding: 6px 10px;
    border-radius: 6px;
    width: 150px;
    display: inline-block;
'>
    {}
</h4>
"""

# KPIs Section
with st.container():
    st.markdown("### 📊 Key Performance Indicators")
    col1, col2, col3, col4, col5, col6 = st.columns(6)

    total_bookings = df.shape[0]
    cancellation_rate = df[df['booking_status'] == 'Canceled'].shape[0] / total_bookings * 100
    cancellation_rate = f"{cancellation_rate:.1f}%"
    avg_price = float(df['avg_price_per_room'].mean())
    avg_lead_time = float(df['lead_time'].mean())
    repeat_rate = float(df['repeated_guest'].mean() * 100)

    col1.markdown(style.format('Total Bookings'), unsafe_allow_html=True)
    col1.metric(label="", value=f"{total_bookings:,}")

    col2.markdown(style.format('Cancellation Rate'), unsafe_allow_html=True)
    col2.metric(label="", value=f"{cancellation_rate}")

    col3.markdown(style.format('Average Price'), unsafe_allow_html=True)
    col3.metric(label="", value=f"{avg_price:.1f} €")

    col4.markdown(style.format('Avg Lead Time'), unsafe_allow_html=True)
    col4.metric(label="", value=f"{avg_lead_time:.1f}")

    col5.markdown(style.format('Repeated Guests'), unsafe_allow_html=True)
    col5.metric(label="", value=f"{repeat_rate:.1f} %")

st.markdown("<br>",unsafe_allow_html=True)
st.markdown("<br>",unsafe_allow_html=True)


# --- Booking Status Pie Chart ---
with st.container():
    col1, col2 = st.columns([1,2])
    booking_counts = df['booking_status'].value_counts().reset_index()
    booking_counts.columns = ['Status', 'Count']

    fig1 = px.pie(booking_counts, names='Status', values='Count',
                  title='Booking Status Overview', hole=0.4)
    col1.plotly_chart(fig1, use_container_width=True)

    # Cancellation Rate by Segment
    cancellation_by_segment = df[df['booking_status'] == 'Canceled']['market_segment_type'].value_counts()
    total_by_segment = df['market_segment_type'].value_counts()
    cancel_rate_segment = (cancellation_by_segment / total_by_segment).fillna(0).sort_values()
    
    cancel_rate_df = cancel_rate_segment.reset_index()
    cancel_rate_df.columns = ['Segments', 'Cancellation Rate']

    fig2 = px.bar(cancel_rate_df,
                  orientation='h',
                  x='Cancellation Rate',
                  y='Segments',
                  title='Cancellation Rate by Segment')
    col2.plotly_chart(fig2,use_container_with=True)

# --- Booking Trends Over Time
with st.container():
    st.markdown("###  📅 Booking Trend Over Time")
    
    # Some refinements to deal with date
    df['arrival_date'] = df['arrival_date'].astype(str)
    df['arrival_month'] = df['arrival_month'].astype(str)
    df['arrival_year'] = df['arrival_year'].astype(str)

    df['Arrival Date'] = df.apply(
    lambda row: f"{row['arrival_year']}-{row['arrival_month']}-{row['arrival_date']}", axis=1
    )

    df['Arrival Date'] = pd.to_datetime(df['Arrival Date'], errors='coerce')

    bookings_by_month = df.dropna(subset=['Arrival Date']).groupby(df['Arrival Date'].dt.to_period('M')).size().reset_index(name='count')
    bookings_by_month['Arrival Date'] = bookings_by_month['Arrival Date'].astype(str)

fig3 = px.line(bookings_by_month, x='Arrival Date', y='count',
               title='Bookings Over Time',
               labels={'arrival_date':'Month', 'count': 'Number of Bookings'})
st.plotly_chart(fig3, use_countainer_width=True)

# --- Segment Filter & Price Distribution ---
with st.container():
    st.markdown("### 🔎 Explore by Market Segment")
    segment = st.selectbox("Select Market Segment:", df['market_segment_type'].unique())
    filtered_df = df[df['market_segment_type'] == segment]

    fig4 = px.histogram(filtered_df,
                        x='avg_price_per_room',
                        nbins=20,
                        title=f"Room Price Distribution – {segment}",
                        labels={'avg_price_per_room': 'Room Price (€)'},
                        marginal="rug")
    st.plotly_chart(fig4, use_container_width=True)