# Load the dataset
data = pd.read_csv('dataset - netflix1.csv')

# Replace missing values with a specific value or strategy for all columns
data.fillna(value=0, inplace=True)  # Replace missing values with 0