
import pandas as pd

import seaborn

# Load the dataset
data = pd.read_csv('dataset - netflix1.csv')

# Replace missing values with a specific value or strategy for all columns
data.fillna(value=0, inplace=True)  # Replace missing values with 0

# Remove outliers for all columns
def remove_outliers_iqr(data, columns):
    for column in columns:
        Q1 = data[column].quantile(0.25)
        Q3 = data[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        data = data[(data[column]>= lower_bound) & (data[column] <= upper_bound)]
        return data
    columns_to_check + ["show_id", "type", "director", "country", "date_added", "release_year", "rating", "duration", "listed_in"]
    data = remove_outliers_iqr(data, columns_to_check)
    

# Save the cleaned dataset
data.to_csv('cleaned2_dataset.csv', index=False)
print("cleaned data is pribted in the terminal and saved as correspond file in the same folder")
print(data)
