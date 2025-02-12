# International Tourist Arrivals Data Analysis

This repository contains a Python script (`International-Tourist-Arrivals.ipynb`) that performs exploratory data analysis (EDA) and visualization on international tourist arrival data.  The analysis uses the Pandas, Matplotlib, and Seaborn libraries.

## Dataset

The dataset used in this analysis is `1-international-Tourist-Arrivals-by-region-of-origin.csv` placed in a `data` directory within the repository.  It contains information on international tourist arrivals by region of origin, year, and the number of arrivals.  The original dataset is sourced from [Kaggle](https://www.kaggle.com/datasets/imtkaggleteam/tourism).

## Code

The Python script `International-Tourist-Arrivals.ipynb` performs the following steps:

1. **Data Loading and Cleaning:** Loads the data from the CSV file using Pandas.  Cleans the data by removing unnecessary columns and handling missing values. Renames columns for better readability.
2. **Exploratory Data Analysis (EDA):** Calculates descriptive statistics and checks data types.
3. **Trend Analysis:** Visualizes the overall trend of international tourist arrivals over time using line plots.  Optionally, it also plots the trend by country/region.
4. **Regional Comparison:** Compares total international tourist arrivals across different regions using bar charts.
5. **Growth Rate Analysis:** Calculates and visualizes the average growth rate of international tourist arrivals for each region.

## Requirements

To run this analysis, you need the following Python libraries:

* Pandas
* Matplotlib
* Seaborn

You can install these libraries using pip:

```
pip install pandas matplotlib seaborn
```

## Output
The script generates the following visualizations:

- Overall trend of international tourist arrivals over time.
- Trend of international tourist arrivals by country/region.
- Total international tourist arrivals by region (bar chart).
- Average growth rate of international tourist arrivals by region (bar chart).


## Contributing
Contributions are welcome!  Please open an issue or submit a pull request.

## License
MIT License

