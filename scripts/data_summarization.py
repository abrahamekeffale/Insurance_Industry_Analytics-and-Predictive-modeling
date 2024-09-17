# scripts/data_summarization.py

import pandas as pd

def summarize_data(df):
    # Descriptive statistics
    print(df.describe())

    # Data types
    print(df.dtypes)

    # Check for missing values
    missing_vals = df.isnull().sum()
    print("Missing Values:\n", missing_vals)

# Example usage
if __name__ == "__main__":
    df = pd.read_csv('../data/your_data.csv')
    summarize_data(df)
