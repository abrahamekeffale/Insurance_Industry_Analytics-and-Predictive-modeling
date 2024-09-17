import os
import pandas as pd

# Define the file paths
data_dir = "data"
txt_file = os.path.join(data_dir, "C:/Users/HP/123/Insurance_Industry_Analytics-and-Predictive-modeling/.venv/data/mydata.txt")
csv_file = os.path.join(data_dir, "C:/Users/HP/123/Insurance_Industry_Analytics-and-Predictive-modeling/.venv/data/mydata.csv")

# Load the .txt file, assuming it's comma-delimited
df = pd.read_csv(txt_file, delimiter="|")  # Adjust delimiter if necessary (e.g., '\t' for tab-delimited)

# Save the data to a new .csv file in the same directory
df.to_csv(csv_file, index=False)

print(f"Data has been successfully saved to {csv_file}")
