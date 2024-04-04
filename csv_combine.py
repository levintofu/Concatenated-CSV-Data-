import os
import pandas as pd

# Specify the directory containing CSV files
csv_directory = r"C:\Users\TC\AppData\Local\Programs\Python\Python310\CSV Combined"

# Get a list of all CSV files in the directory
csv_files = [file for file in os.listdir(csv_directory) if file.lower().endswith(".csv")]

# Initialize an empty DataFrame to store combined data
combined_df = pd.DataFrame()

# Read each CSV file and concatenate its data to the combined DataFrame
for csv_file in csv_files:
    file_path = os.path.join(csv_directory, csv_file)
    df = pd.read_csv(file_path)
    combined_df = pd.concat([combined_df, df], ignore_index=True)

# Save the combined DataFrame to a new CSV file
combined_csv_path = "C:/Users/TC/AppData/Local/Programs/Python/Python310/CSV Combined/combined.csv"
combined_df.to_csv(combined_csv_path, index=False)

# Print a success message
print(f"Combined data from {len(csv_files)} CSV files and saved to {combined_csv_path}")