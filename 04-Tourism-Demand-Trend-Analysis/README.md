# Tourism Demand Trend Analysis (SQL Project)
This project analyzes how tourism capacity and demand indicators have evolved over time across the world, using data from the [UNWTO Tourism Dataset](https://webunwto.s3.eu-west-1.amazonaws.com/s3fs-public/2021-08/unwto-tourism-industries-data.xlsx). The project demonstrates SQL querying skills within a Jupyter environment and includes data cleaning, analysis, and trend visualization.

### Project Structure
````
Tourism-Demand-Analysis/
├── data-cleaning.ipynb          # Preprocessing and reshaping of the raw Excel file
├── sql-analysis.ipynb           # SQL queries run on cleaned data using ipython-sql
├── unwto_cleaned_long.csv       # Final cleaned long-format dataset
├── README.md
````

### Objective
To explore the question:

**"How have tourism capacities and demand indicators changed over time across the world?"**

We focus primarily on:

- **Tourism Capacity**: Number of bed-places
- **Tourism Demand**: Occupancy rate of bed-places

#### Step 1: Data Cleaning
Conducted in data-cleaning.ipynb, which includes:

- Loading multi-sheet Excel from UNWTO
- Skipping metadata rows
- Renaming and reshaping columns
- Creating a long-format CSV (unwto_cleaned_long.csv)

#### Step 2: SQL Analysis in Jupyter
All SQL is executed in sql-analysis.ipynb using ipython-sql and sqlite3.

#### Key Findings
- Tourism capacity (measured in number of bed-places) has generally increased across the world since 1995.
- Occupancy rates show fluctuation, indicating varying levels of demand despite rising capacity.
- Some countries have shown exponential growth in infrastructure, while others remain stagnant.

#### Tech Stack
- Python (Pandas, SQLite)
- Jupyter Notebook
- ipython-sql
- SQL (SQLite dialect)

#### How to Run
1. Clone this repository:
````
git clone https://github.com/Fsepehrpour/Tourism-Analytics/tree/3852e620aff3a195dea2c029c904f9c3fdc105ed/04-Tourism-Demand-Trend-Analysis
````

2. Open the notebooks in Jupyter:
````
Jupyter Lab
````

3. Run data-cleaning.ipynb to generate the cleaned CSV.
4. Run sql-analysis.ipynb to execute the analysis and visualize results.

#### Author
Fatemeh Sepehrpour
[LinkedIn](www.linkedin.com/in/fatemeh-sepehrpour-012982ba)



