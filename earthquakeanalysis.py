import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load earthquake data from CSV file
data = pd.read_csv('earthquake_data.csv')

# Get basic information about the dataset
print(data.info())

# Get summary statistics about the magnitude column
print(data['magnitude'].describe())

# Plot a histogram of earthquake magnitudes
plt.hist(data['magnitude'], bins=20)
plt.xlabel('Magnitude')
plt.ylabel('Count')
plt.show()

# Group the data by year and calculate the average magnitude for each year
yearly_data = data.groupby('year').mean()['magnitude']
print(yearly_data)

# Plot a line graph of average yearly magnitudes
plt.plot(yearly_data.index, yearly_data.values)
plt.xlabel('Year')
plt.ylabel('Average Magnitude')
plt.show()


#In this code, we first load earthquake data from a CSV file using the Pandas read_csv function. We then print some basic information about the dataset using the info method and summary statistics about the magnitude column using the describe method.We then plot a histogram of earthquake magnitudes using Matplotlib's hist function. Next, we group the data by year using Pandas' groupby method and calculate the average magnitude for each year. We then plot a line graph of average yearly magnitudes using Matplotlib's plot function.