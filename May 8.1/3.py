import pandas as pd#import necessary lib
import numpy as np

# Load the dataset
df = pd.read_csv('/home/minnu/Desktop/week 1/may 8/Sample - Superstore.csv', encoding='ISO-8859-1')

# Use only numeric data
data = df.select_dtypes(include=[np.number])

# Print mean, median, and standard deviation
print("Mean:\n", data.mean())
print("\nMedian:\n", data.median())
print("\nStandard Deviation:\n", data.std())