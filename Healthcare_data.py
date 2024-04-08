import pandas as pd

# Load the datasets into pandas DataFrames
data_breaches = pd.read_csv(r'C:\\Users\\anjum\\OneDrive\\Desktop\\Case Studies\\Project\\data_breaches.csv')
healthcare_data_breaches = pd.read_csv(r'C:\\Users\\anjum\\OneDrive\\Desktop\\Case Studies\\Project\\Healthcare_Data_Breaches.csv')

# Define a mapping dictionary to map columns from one dataset to the other
column_mapping = {
    'Name of Covered Entity': 'Name',
    'Covered Entity Type': 'Entity Type',
    'Individuals Affected': 'Individuals Affected',
    'Breach Submission Date': 'Year',
    'Type of Breach': 'Type',
    'State': 'State',
    'Location of Breached Information': 'Location of Breached Information'
}

# Rename columns in data_breaches DataFrame based on the mapping
data_breaches.rename(columns=column_mapping, inplace=True)

# Select only the required columns from healthcare_data_breaches
healthcare_data_breaches = healthcare_data_breaches[['Name', 'Entity Type', 'Individuals Affected', 'Year', 'Type']]

# Concatenate or merge the DataFrames based on common columns or indices
consolidated_data = pd.concat([data_breaches, healthcare_data_breaches])

# Optionally, handle missing values or duplicates
consolidated_data.drop_duplicates(inplace=True)

# Save the consolidated DataFrame to a new CSV file or Excel file
consolidated_data.to_csv('Health_consolidated_data.csv', index=False)
# or consolidated_data.to_excel('consolidated_data.xlsx', index=False)

# Display the first few rows of the consolidated DataFrame
print(consolidated_data.head())

consolidated_data.to_csv('C:\\Users\\anjum\\OneDrive\\Desktop\\Case Studies\\Project\\Health_consolidated_data.csv', index=False)
