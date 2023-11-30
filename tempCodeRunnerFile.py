elease_year", "rating", "duration", "listed_in"]
    data = remove_outliers_iqr(data, columns_to_check)
    

# Save the cleaned dataset
data.to_csv('cleaned2_dataset.csv', index=False)
print("cleaned data is pribted in the terminal and saved as correspond file in the same folder")
print(data)
