# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset (make sure the CSV is in the same folder)
df = pd.read_csv('/home/minnu/Desktop/week 1/may 8/Sample - Superstore.csv', encoding='ISO-8859-1')

# STEP 1: Basic Data Inspection

print("\n--- First 5 Rows ---")
print(df.head())

print("\n--- Dataset Info ---")
print(df.info())

print("\n--- Summary Statistics ---")
print(df.describe(include='all'))


#  STEP 2: Convert Dates to Datetime

df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])


#  STEP 3: Check Missing Values

print("\n--- Missing Values Per Column ---")
print(df.isnull().sum())


#  STEP 4: Basic Analysis & Filtering


# Filter example: All orders from California
california_orders = df[df['State'] == 'California']
print("\n--- Orders from California ---")
print(california_orders.head())

#  STEP 5: Sorting and Grouping


# Top 5 sales records
top_sales = df.sort_values(by='Sales', ascending=False).head()
print("\n--- Top 5 Sales Records ---")
print(top_sales[['Product Name', 'Sales', 'Profit']])

# Total sales and profit by category
category_summary = df.groupby('Category')[['Sales', 'Profit']].sum()
print("\n--- Total Sales & Profit by Category ---")
print(category_summary)


#  STEP 6: Value Counts Example

print("\n--- Ship Mode Counts ---")
print(df['Ship Mode'].value_counts())

#  STEP 7: Pivot Table and Correlation


# Profit by Region and Category
pivot = df.pivot_table(values='Profit', index='Region', columns='Category', aggfunc='sum')
print("\n--- Pivot Table: Profit by Region & Category ---")
print(pivot)

# Correlation matrix (numeric columns only)
correlation = df[['Sales', 'Quantity', 'Discount', 'Profit']].corr()
print("\n--- Correlation Matrix ---")
print(correlation)


# Heatmap of correlation matrix
plt.figure(figsize=(8, 6))
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.show()
