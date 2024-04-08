import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv(r'C:\\Users\\anjum\\OneDrive\\Desktop\\Case Studies\\Project\\5.12_Cybersecurity_(detail).csv')  

# Display the first 5 rows of the DataFrame
print("First 5 rows of the DataFrame:")
print(df.head())

# Check data types of columns
print("\nData types of columns:")
print(df.dtypes)

# Generate summary statistics for numerical columns
print("\nSummary statistics for numerical columns:")
print(df.describe())

# Display unique values for categorical columns
print("\nUnique values for categorical columns:")
print("Control_Set:", df['Control_Set'].unique())
print("Control_Family_Code:", df['Control_Family_Code'].unique())

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

# Check the number of rows and columns
print("\nNumber of rows and columns:")
print(df.shape)
