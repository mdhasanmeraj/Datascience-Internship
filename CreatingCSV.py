#Create a CSV dataset using Python, Pandas and any public api

#importing pandas and requests for using json
import pandas as pd
import requests

# Make a request to the public API
response = requests.get('https://api.publicapis.org/entries')
#We only the CSV file for the 'entries' section of the given api
response.json()['entries']
data = response.json()['entries']

# Create a DataFrame using the data
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('data.csv', index=False, )
print('CSV file is saved in your device and also print in the terminal')
print(df)