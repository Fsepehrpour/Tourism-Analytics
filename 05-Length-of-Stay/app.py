import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# set Streamlit page title
st.set_page_config(page_title="Analysis of Average Length of Stay", layout="wide")

# Load the dataset
@st.cache_data
def load_data():
    df = pd.read_csv("../data/10- average-length-of-stay.csv")
    return df

df = load_data()


# Sidebar filters
st.sidebar.header("Filter Data")
selected_country = st.sidebar.selectbox("Select a country", df["Entity"].unique())
selected_year = st.sidebar.slider("Select year", int(df["Year"].min()), int(df["Year"].max()), (int(df["Year"].min()), int(df["Year"].max())))

# Filtered data
filtered_df = df[(df["Entity"] == selected_country) & (df["Year"].between(selected_year[0], selected_year[1]))]

# Title
st.title("🌍 Analysis of Average Length of Stay")

# Show dataset
if st.checkbox("Show Raw Data"):
    st.write(df.head())

# **1. Distribution of Average Length of Stay**
st.subheader("📊 Distribution of Average Length of Stay")
fig, ax = plt.subplots(figsize=(8, 5))
sns.histplot(df["Average length of stay"], bins=30, kde=True, ax=ax)
plt.xlabel("Average Length of Stay (Days)")
plt.ylabel("Frequency")
st.pyplot(fig)

# **2. Yearly Trends for Selected Country**
st.subheader(f"📈 Yearly Trend: {selected_country}")
fig, ax = plt.subplots(figsize=(8, 5))
filtered_yearly_df = df[df["Entity"] == selected_country]
ax.plot(filtered_yearly_df["Year"], filtered_yearly_df["Average length of stay"], marker="o", linestyle="-", color="orange")
plt.xlabel("Year")
plt.ylabel("Average Length of Stay")
plt.title(f"Trend of Average Length of Stay in {selected_country}")
st.pyplot(fig)

# **3. Top Countries with the Longest Stay Durations**
st.subheader("🌎 Top Countries by Average Length of Stay")
top_countries = df.groupby("Entity")["Average length of stay"].mean().sort_values(ascending=False).head(10)
st.bar_chart(top_countries)

# **4. Heatmap of Stay Durations by Country & Year**
st.subheader("📊 Heatmap: Average Stay Duration by Country and Year")
pivot_df = df.pivot(index="Entity", columns="Year", values="Average length of stay").fillna(0)
fig, ax = plt.subplots(figsize=(12, 8))
sns.heatmap(pivot_df, cmap="coolwarm", annot=False, linewidths=0.5)
plt.xlabel("Year")
plt.ylabel("Country")
st.pyplot(fig)

# Footer
st.markdown("💡 *This dashboard provides insights into tourism stay durations. Data source: [Your Data Source]*")
