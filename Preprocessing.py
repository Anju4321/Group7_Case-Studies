import pandas as pd
import numpy as np

# Load the CSV file into a DataFrame with specified encoding
df = pd.read_csv(r'C:\\Users\\anjum\\OneDrive\\Desktop\\Case Studies\\Project\\preprocessed_dataV0.1.csv', encoding='ISO-8859-1')

# Fill missing values in specific columns using direct assignment
df['Individuals Affected'] = df['Individuals Affected'].fillna(np.nan)
df['State'] = df['State'].fillna('Unknown')
df['Location of Breached Information'] = df['Location of Breached Information'].fillna('Unknown')
df['Business Associate Present'] = df['Business Associate Present'].fillna('Unknown')

# Convert 'Breach Submission Date' column to datetime
# df['Breach Submission Date'] = pd.to_datetime(df['Breach Submission Date'], errors='coerce')  # Adjust format if needed

# Convert 'Breach Submission Date' column to datetime with inferred format
df['Breach Submission Date'] = pd.to_datetime(df['Breach Submission Date'], errors='coerce', infer_datetime_format=True)

# 3. Cleaning Text Data
# Example: Convert text data to lowercase and remove leading/trailing spaces
df['Name of Covered Entity'] = df['Name of Covered Entity'].str.lower().str.strip()

# Extract year from 'Breach Submission Date' and store in 'Year' column
df['Year'] = df['Breach Submission Date'].dt.year

# 4. Addressing Rank Column Issues
#df['Rank'] = df['Rank'].str.replace('#', '')  # Remove '#' from rank values

# Split the 'State' column at '/' and extract the first word to create 'Type of Breach' column
df['Type of Breach'] = df['State'].str.split('/').str[0]

# Check if '/' is present in the 'State' column
has_slash = df['State'].str.contains('/')

# Remove '/' and the strings before '/' from the 'State' column only if '/' is present
df.loc[has_slash, 'State'] = df.loc[has_slash, 'State'].str.split('/').str[1]

# 5. Exploring and Visualizing Data (optional)
# Perform exploratory data analysis and visualization using libraries like matplotlib or seaborn

# 6. Feature Engineering 
# Example: Derive year from the Breach Submission Date column
df['Year'] = df['Breach Submission Date'].dt.year

# 7. Encoding Categorical Variables (if needed)
# Example: Perform one-hot encoding for categorical variables
#df = pd.get_dummies(df, columns=['Type of Breach', 'Covered Entity Type'])

# 8. Handling Duplicate Data (if applicable)
df.drop_duplicates(inplace=True)

# 9. Scaling Numerical Data (if needed)
# Example: Scale numerical columns using Min-Max scaling or Standardization

# 10. Final Data Inspection
# Perform final inspection of the preprocessed data
print(df.info())
print(df.describe())

# Optionally, save the preprocessed data to a new CSV file
df.to_csv(r'C:\\Users\\anjum\\OneDrive\\Desktop\\Case Studies\\Project\\preprocessed_dataV0.2.csv', index=False)
