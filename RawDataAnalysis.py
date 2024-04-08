import pandas as pd

# Load the CSV file into a DataFrame
import pandas as pd

# Load the CSV file into a DataFrame with specified encoding
df = pd.read_csv(r'C:\\Users\\anjum\\OneDrive\\Desktop\\Case Studies\\Project\\Health_consolidated_data.csv', encoding='ISO-8859-1')

# Display the first few rows of the DataFrame
print(df.head())


# Display the first 5 rows of the DataFrame
print("First 5 rows of the DataFrame:")
print(df.head())

# Check data types of columns
print("\nData types of columns:")
print(df.dtypes)

# Generate summary statistics for numerical columns
print("\nSummary statistics for numerical columns:")
print(df.describe())

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

# Check the number of rows and columns
print("\nNumber of rows and columns:")
print(df.shape)
