# import python libraries
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns


# Load the dataset
df = pd.read_csv('dataset - netflix1.csv')
print("Dataset is ready for the further work")


# Replace missing values with a specific value or strategy for all columns
df.fillna(value=0, inplace=True)  # Replace missing values with 0


# Identify and clean outliers in the numeric columns
numeric_columns = df.select_dtypes(include=np.number).columns
for column in numeric_columns:
    q1 = df[column].quantile(0.25)
    q3 = df[column].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    df = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
    
    print(df)
    
    
# Explore the data
print(df.head())  # Display the first few rows of the dataset
print(df.info())  # Get information about the dataset

#Analyzing the dataset and making graphs according to the release_year and rating

columns = ['show_id','type','title','director','country','date_added','release_year','rating','duration','listed_in'] 
# Bar plot
sns.barplot(x='release_year', y='rating', data=df)
plt.xlabel('release_year')
plt.ylabel('rating')
plt.title('Bar_Plot')
plt.show()

# Line plot
sns.lineplot(x='release_year', y='rating', data=df)
plt.xlabel('release_year')
plt.ylabel('rating')
plt.title('Line_plot')
plt.show()

# Scatter plot
sns.scatterplot(x='release_year', y='rating', data=df)
plt.xlabel('release_year')
plt.ylabel('rating')
plt.title('Scatter_Plot')
plt.show()

# Histogram
sns.histplot(data=df, x='release_year')
plt.xlabel('release_year')
plt.title('Histogram_plot')
plt.show()

# Box plot
sns.boxplot(x='release_year', y='rating', data=df)
plt.xlabel('release_year')
plt.ylabel('title')
plt.title('Box_plot')
plt.show()

