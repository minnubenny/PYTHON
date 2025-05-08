# Bar chart of total sales by category


import pandas as pd# Import libraries
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('/home/minnu/Desktop/week 1/may 8/Sample - Superstore.csv', encoding='ISO-8859-1')# Load the dataset-encoding is used bcz the dataset contained special characters so to avoid errors.

print(df.head())# Step 1: Inspect the data
print(df.info())


category_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)# Step 2: Group data by Category and sum Sales
print("\n--- Total Sales by Category ---")
print(category_sales)


plt.figure(figsize=(8, 6))  # Step 3: Plot        # Set chart size
category_sales.plot(kind='bar', color='skyblue')  # Bar chart
plt.title('Total Sales by Category')              # Title
plt.xlabel('Category')                            # X-axis label
plt.ylabel('Total Sales')                         # Y-axis label
plt.xticks(rotation=45)                           # Rotate x labels
plt.grid(axis='y', linestyle='--', alpha=0.7)     # Add horizontal grid lines
plt.tight_layout()                                # Adjust layout
plt.show()