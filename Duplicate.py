import pandas as pd
from dateutil.parser import parse

# Load your CSV file
df = pd.read_csv('mydata.csv')

# Remove duplicate rows
df = df.drop_duplicates()

# Convert 'timestamp' column to datetime and handle multiple formats
df['timeframe'] = df['timestamp'].apply(parse)

# Sort by timeframe from oldest to newest
df = df.sort_values('timeframe')

# Save the result to a new CSV file
df.to_csv('sorted_file.csv', index=False)
