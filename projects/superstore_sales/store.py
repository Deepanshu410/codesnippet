import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

'''# Create realistic retail data
np.random.seed(42)
n_rows = 500
categories = ['Electronics', 'Furniture', 'Office Supplies', 'Clothing']
regions = ['North', 'East', 'South', 'West']
start_date = datetime(2025, 1, 1)

data = []
for _ in range(n_rows):
    cat = np.random.choice(categories)
    region = np.random.choice(regions)
    sales = round(float(np.random.exponential(scale=200) + 10), 2)
    profit = round(sales * np.random.uniform(-0.2, 0.5), 2)
    date = (start_date + timedelta(days=int(np.random.randint(0, 365)))).strftime('%Y-%m-%d')
    
    # Intentionally corrupt 25 rows of Profit data to create missing values
    if np.random.rand() < 0.05:
        profit = np.nan
        
    data.append([date, cat, region, sales, profit])

# Save as a CSV file on your machine
df = pd.DataFrame(data, columns=['Order_Date', 'Category', 'Region', 'Sales', 'Profit'])
df.to_csv('superstore_sales.csv', index=False)
print("Data generated! 'superstore_sales.csv' is ready for your project.")
'''

# Part A: Data Cleaning (Pandas & NumPy)
df = pd.read_csv('superstore_sales/superstore_sales.csv')
#print(df) # order date, category, region, sales, profit
#print(df.info()) # check for missing values (Pandas)
#print(df.describe()) # summary Statistics (Pandas)
#print(df.isnull().sum()) # Find the Missing Data (NumPy/Pandas)
#df['Profit'] = df['Profit'].fillna(0) # Fix Missing Rows (NumPy/Pandas)

# Part B: Answering Business Questions (Pandas)
# Find Total Performance:
total_profit = df['Profit'].sum() 
total_sales = df['Sales'].sum()
print(f'Total Profit: ${total_profit:,.2f}')
print(f'Total Sales: ${total_sales:,.2f}')
# Calculate sales broken down by each product category;
category_sales = df.groupby('Category')['Sales'].sum()
print(category_sales)
# Filter for Losses:
loss_df = df[df['Profit'] < 0]
print(loss_df.head())

# Part C: Visualizing Findings (Matplotlib & Seaborn);
# Create the Canvas (Matplotlib);
plt.figure(figsize=(10, 5))
# Draw a Bar Chart (Seaborn);
sns.barplot(data=df, x='Category', y='Sales', estimator=sum)
# Add Context (Matplotlib):
plt.title("Total Sales by Category") 
plt.grid(axis='y', alpha=0.3)
plt.show()

# Can you find the total sales grouped by Region instead of Category?
category_sales2 = df.groupby('Region')['Sales'].sum()
print(category_sales2)
# Can you find the average (.mean()) profit per category instead of the sum?
category_sales3 = df.groupby('Category')['Sales'].mean()
print(category_sales3)
# Can you filter the data for orders where sales were greater than 500 (df['Sales'] > 500)?
sales_g = df[df['Sales'] > 500]
print(sales_g.head())


# C

# 1. Subplots: Create a canvas layout with 1 row and 2 columns. Set figsize=(14, 5)
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# 2. Left Chart: Use sns.barplot on axes[0] to show total Sales by Category
# Hint: x='Category', y='Sales', data=df, ax=axes[0], estimator=sum, errorbar=None
sns.barplot(x='Category', y='Sales', data=df, ax=axes[0], estimator=sum, errorbar=None)

# 3. Left Chart Polish: Add a title and grid lines to axes[0] using your notes
axes[0].set_title('Total Sales by Category')
axes[0].grid(axis='y', linestyle='--', alpha=0.5)

# 4. Right Chart: Use sns.barplot on axes[1] to show total Sales by Region
# Hint: x='Region', y='Sales', data=df, ax=axes[1], estimator=sum, errorbar=None
sns.barplot(x='Region', y='Sales', data=df, ax=axes[1], estimator=sum, errorbar=None)

# 5. Right Chart Polish: Add a title and grid lines to axes[1]
axes[1].set_title('Total Sales by Region')
axes[1].grid(axis='x', linestyle='-', alpha=0.5)

# 6. Clean Layout: Fix spacing and display
plt.tight_layout()
plt.show()
