import pandas as pd

# Read the Excel file into a DataFrame
file_path = 'Book1.xlsx'
df = pd.read_excel(file_path)

# Convert the DataFrame to a dictionary
records_dict = df.to_dict(orient='records')

print(records_dict)