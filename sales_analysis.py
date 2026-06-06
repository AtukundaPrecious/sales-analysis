import pandas as pd

# Load dataset (same folder as script)
df = pd.read_csv("sales_analysis.csv", encoding="latin1")

# Preview data
print("First 5 rows:")
print(df.head())

# Dataset information
print("\nDataset Info:")
print(df.info())

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

print("\nSummary Statistics:")
print(df.describe())

print("\nColumn Names:")
print(df.columns)

print("\nTotal Sales:")
print(df["Sales"].sum())

print("\nTotal Profit:")
print(df["Profit"].sum())

print("\nTop 10 Sales:")
print(df.nlargest(10, "Sales")[["Sales", "Profit"]])

print("Total Sales:")
print(df["Sales"].sum())

print("\nTotal Profit:")
print(df["Profit"].sum())

# Sales by Category
print("\nSales by Category:")
print(df.groupby("Category")["Sales"].sum().sort_values(ascending=False))

# Profit by Category
print("\nProfit by Category:")
print(df.groupby("Category")["Profit"].sum().sort_values(ascending=False))

# Sales by Region
print("\nSales by Region:")
print(df.groupby("Region")["Sales"].sum().sort_values(ascending=False))

# Top 10 Products by Sales
print("\nTop 10 Products by Sales:")
print(
    df.groupby("Product Name")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

# Most Profitable Products
print("\nTop 10 Products by Profit:")
print(
    df.groupby("Product Name")["Profit"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

# Least Profitable Products
print("\nTop 10 Loss-Making Products:")
print(
    df.groupby("Product Name")["Profit"]
      .sum()
      .sort_values()
      .head(10)
)

import matplotlib.pyplot as plt

category_sales = df.groupby("Category")["Sales"].sum()

category_sales.plot(kind="bar")
plt.title("Sales by Category")
plt.ylabel("Sales")
plt.show()