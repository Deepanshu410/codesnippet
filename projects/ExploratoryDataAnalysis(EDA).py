# This entire workflow is collectively called Exploratory Data Analysis (EDA). It is the essential first phase of any data science project where you investigate a dataset to understand its patterns, clean its anomalies, and summarize its main characteristics using visual methods. If you break it down into its specific sub-phases, the professional industry terms are:
# 1. Data Cleaning (or Data Cleansing); What it covers: Handling missing values (fillna, dropna), removing duplicates (drop_duplicates), and correcting mismatched data types (astype). The Goal: Fixing errors and formatting inconsistencies so your analysis is accurate.
# 2. Data Wrangling (or Data Munging); What it covers: Slicing, filtering (Boolean indexing), renaming columns, and restructuring data arrays.The Goal: Transforming raw, messy data into a convenient format for analysis.
# 3. Feature Engineering; What it covers: Combining existing columns to create brand new ones (like creating total_income from salary and bonus).The Goal: Creating new variables that expose hidden patterns to make machine learning models smarter.
# 4. Data Visualization; What it covers: Generating charts (sns.countplot, histograms, scatter plots) to spot trends visually. The Goal: Communicating insights instantly to stakeholders or team members

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
df = sns.load_dataset('titanic')

# ==========================================
# 1. Data Exploration and Inspection
# ==========================================
print(df.head(10)) # first 10 rows
print(df.tail(10)) # last 10 rows
print(df.describe()) # statistical summary for all numeric columns
print(df.info(10)) # total rows, columns, rows, and data types
print(df.shape) # dimensions of dataset matrix
print(df.columns) #  cleans list of column names.
print(df.nunique()) # for How many unique values exist in each column
print(df['sex'].value_counts()) # Count specific column category frequencies

# ==========================================
# 1.5 Combining Datasets (Merge & Concat)
# ==========================================
# Mock dataset to simulate passenger contact info
contact_data = {
    'passenger_id': list(range(len(df))),
    'email': [f'passenger{i}@email.com' for i in range(len(df))]
}
df_contact = pd.DataFrame(contact_data)
df['passenger_id'] = range(len(df)) # Add matching ID to main df

# MERGE: Combine tables side-by-side using a shared ID column
df = pd.merge(df, df_contact, on='passenger_id', how='left')

# CONCAT: Stack identical tables vertically (e.g., adding a new batch of 2 rows)
new_rows = pd.DataFrame([{'sex': 'male', 'age': 30}, {'sex': 'female', 'age': 25}])
df = pd.concat([df, new_rows], ignore_index=True)

# Combining Datasets (pd.merge and pd.concat); Real projects often require combining data from multiple sources (like joining user profiles with their transaction logs).
# pd.merge(df, df_contact, on='passenger_id', how='left'): This acts like a SQL Join or a VLOOKUP in Excel. It searches both dataframes for matching values in the passenger_id column and matches them together side-by-side. The how='left' flag ensures you keep all rows from your primary dataset (df) even if they don't have a matching email in the contact sheet.
# pd.concat([df, new_rows], ignore_index=True): This stacks dataframes on top of each other. If you get a new batch of data (e.g., records from a new day), you append them directly to your existing dataframe. ignore_index=True resets the index numbering so it continues smoothly (0, 1, 2, 3...) instead of restarting at 0 for the new batch.
# pd.merge made your dataset WIDER (added columns side-by-side).
# pd.concat made your dataset LONGER (added rows top-to-bottom).

# ==========================================
# 2. Cleaning
# ==========================================
df.isnull().sum() # Count missing values per column
df.dropna(subset=['embarked']) # Completely drop rows where a critical column ('embarked') has missing values

# Fill missing values properly (Pass the computed mean/mode inside fillna())
df['age'] = df['age'].fillna(df['age'].mean())
df['embark_town'] = df['embark_town'].fillna(df['embark_town'].mode()[0]) # mode = the common item
# The zero index [0] is required because the .mode() method in Pandas always returns a Series (a list-like collection), rather than a single direct value. Even if there is only one most common item, Pandas still packages it inside a list. Passing a list directly into .fillna() will cause a formatting error, so you use [0] to pull the actual text value out of that list. 

print(df.duplicated().sum()) # Check for completely identical rows
df = df.drop_duplicates()    # Delete those duplicated row

df['fare'] = df['fare'].astype(int) # Change data types (e.g., converting float 'fare' to integer)
df['deck'] = df['deck'].astype(str).str.strip()  # cleaning up text columns by removing accidental trailing spaces (Must access the string accessor .str on a specific column)
df['class'] = df['class'].astype(str).str.lower()  # making everything lowercase so they match. 

# ==========================================
# 2.5 Advanced Text, Dates, and Outliers
# ==========================================
# TEXT: Search for rows containing a specific keyword (case-insensitive)
has_miss = df['embark_town'].str.contains('queenstown', na=False, case=False)
# This line searches through the embark_town column to find any rows that mention the word "queenstown". Instead of giving you a new table, it generates a long list of True and False values (one for every row). na=False: This is a safety switch. If a passenger has a missing value (NaN) in their town column, .str.contains() gets confused because it cannot search for text inside a blank space. Setting na=False tells Pandas: "If you hit a blank row, don't crash; just mark it as False."case=False: This makes the search case-insensitive. It ensures that "Queenstown", "queenstown", and "QUEENSTOWN" are all successfully caught.

# TEXT: Clean and replace text characters (e.g., standardizing text labels)
df['sex'] = df['sex'].map({'female': 'woman', 'male': 'man'})

# DATES: Convert text columns into true DateTime objects
# (Using dummy dates since Titanic lacks a native timestamp)
df['travel_date'] = '2026-04-10'  
df['travel_date'] = pd.to_datetime(df['travel_date'])

# DATE ACCESSOR: Extract parts of the date instantly
df['travel_year'] = df['travel_date'].dt.year
df['travel_month'] = df['travel_date'].dt.month
df['day_name'] = df['travel_date'].dt.day_name()

# OUTLIERS: Cap extreme ticket prices to prevent distorted metrics
# Anything above the 99th percentile gets dropped down to the 99th percentile value
q_high = df['ticket_price'].quantile(0.99)
df['ticket_price'] = df['ticket_price'].clip(upper=q_high)

# Advanced Text and Date Tools
# df['col'].str.contains('keyword'): This returns True or False for every single row. It is incredibly useful for filtering datasets based on partial words (e.g., finding all text entries containing "Street" or checking if an email is a "@gmail.com" address).
# pd.to_datetime(): By default, computers read dates like "2026-04-10" as plain text strings. Converting them with pd.to_datetime() turns them into native timestamp objects, allowing pandas to understand the chronological relationship between dates.
# The .dt accessor: Once a column is officially converted to a DateTime object, you unlock the .dt toolkit. This lets you extract parts of the date instantly (e.g., getting the month, the year, or naming the specific day of the week like "Friday") without doing manual text slicing.
# Managing Outliers 
# (df.clip)df['fare'].quantile(0.99): This calculates the 99th percentile cutoff mark. It tells you the exact value that 99% of your data falls below.
# df['fare'].clip(upper=q_high): Outliers (like someone paying $500 for a ticket when everyone else paid $10) throw off statistical averages and skew graphs. Instead of deleting these rows completely, clip caps extreme values. Any price higher than the 99th percentile gets automatically changed down to match the cutoff value.


# ==========================================
# 3. Data Manipulation & Transformation
# ==========================================
filtered_df = df[(df['age'] > 25) & (df['sex'] == 'female')] # Boolean filtering; isolate specific data points using conditions (Titanic uses 'sex', not 'gender')

df = df.drop(['alive', 'embarked', 'class'], axis=1) # Delete columns that are completely useless for analysis (like user IDs or random URLs)

df = df.rename(columns={'sex': 'gender', 'fare': 'ticket_price'}) 

df['family_size'] = df['sibsp'] + df['parch'] + 1 # combine existing columns to make new ones (Using dummy numbers since Titanic lacks salary/bonus)

df = df.sort_values(by='column_name', ascending=False) # sort entire dataset based on a specific column

# ==========================================
# 4. Advanced Grouping & Aggregation (finding patterns)
# ==========================================
print(df.groupby('gender')['ticket_price'].mean())  # group by one column and find average of another (Using updated column names)
print(df.groupby(['who', 'gender'])['ticket_price'].mean())  # group by multiple layers
print(df.groupby('who')['age'].agg(['min', 'max', 'mean', 'median'])) # Multiple aggregate metrics at once

# ==========================================
# 4.5 Reshaping Tables (Pivoting & Melting)
# ==========================================
# PIVOT TABLE: Create a spreadsheet-style grid summary (Rows: class, Columns: sex, Values: average ticket price)
pivot_summary = df.pivot_table(index='pclass', columns='gender', values='ticket_price', aggfunc='mean')
print(pivot_summary)

# MELT: Take a wide summary table and unpivot it back into a long format
# Useful for preparing data for specific charting libraries
melted_df = pd.melt(df, id_vars=['passenger_id'], value_vars=['age', 'ticket_price'], var_name='metric', value_name='value') # value_vars = variables you want to stack, var_name = variable name under which the value_vars are stacked, value_name= variable name under which actual values would be stored.

# Reshaping Tables (pivot_table and melt)
# df.pivot_table(): This works exactly like a Pivot Table in Excel. It creates a matrix summary grid. You define what goes on the rows (index), what goes on the columns (columns), and what math function to run (aggfunc) on the values.
# pd.melt(): This does the exact opposite of a pivot table. It takes wide columns (like a column for age and a column for ticket_price) and collapses them down into a narrow, long list of key-value pairs. This "long format" is the standard layout required by advanced visualization tools. transforming your data from a wide format (where variables have their own columns) into a long format (where variables are stacked vertically into rows).


# ==========================================
# 5. Visualization
# ==========================================
sns.countplot(x='class', data=df) # (Categorical Frequency) Draw a bar chat showing the frequence of text categories [Three bars (First, Second, Third) showing exactly how many passengers were in each ticket class.]

sns.histplot(x='age', data=df, kde=True) #  (Numerical Distribution) see the distribution and spread of a numeric column (kde=True adds a smooth trend line over the bars). [A tower of bars showing how many people were 0–10 years old, 10–20 years old, etc., with a smooth wave line tracking the overall age trend.]

sns.boxplot(x='category', y='numeric_column', data=df) #  (Category vs. Number) x = category, y=numeric_column prefect for comparing groups and spotting extreme outliers [Three boxes side-by-side. It lets you visually compare if First Class passengers were generally older than Third Class passengers, with dots showing age outliers.]

sns.scatterplot(x='age', y='ticket_price', hue='alive', data=df) # (Number vs. Number + Color) x='col1', y='col2', hue='category', compare two numbers against each other, using the hue argument to color-code the points based on a text category. [A cloud of dots mapped by age and ticket price. The dots will be colour-coded (e.g., blue for "yes", orange for "no") so you can see if young, wealthy passengers survived more.]

sns.heatmap(df.corr(numeric_only=True), annot=True) # (Correlatin matrix heatmap). It shows exactly which number move together (closer to 1 or -1 means a strong relationship, closer to 0 means no relationship) [For example, the intersection of fare and pclass will show a strong negative number (around -0.55), proving that as class number goes down (1st class), the ticket price goes up.]
# A correlation measures how two variables move together, while a matrix is an organized grid of numbers. Together, a correlation matrix is a table that displays the correlation coefficients between multiple variables, allowing you to instantly spot patterns and relationships in a large dataset.

plt.show()




# Automating the Workflow into Reusable FunctionsInstead of copy-pasting your code every time you get a new dataset, you can bundle your steps into a dedicated Python function. This makes your code modular, readable, and reusable.Here is how you write and execute a standardized data cleaning pipeline:

# ==========================================
# Defining the Automation Pipeline Function
# ==========================================
import pandas as pd
import numpy as np

def universal_clean_and_process(raw_dataframe):
    """
    Dynamically cleans and processes ANY dataframe by analyzing its data types,
    filling missing values, capping outliers, and cleaning string fields.
    """
    working_df = raw_dataframe.copy()
    
    # 1. DYNAMICALLY DETECT DATA TYPES
    numeric_cols = working_df.select_dtypes(include=[np.number]).columns.tolist()
    text_cols = working_df.select_dtypes(include=['object', 'category']).columns.tolist()
    
    # 2. UNIVERSAL MISSING VALUE HANDLING
    # Fill numeric missing values with mean
    for col in numeric_cols:
        if working_df[col].isnull().any():
            working_df[col] = working_df[col].fillna(working_df[col].mean())
            
    # Fill text missing values with mode (most frequent item)
    for col in text_cols:
        if working_df[col].isnull().any():
            mode_value = working_df[col].mode()
            if not mode_value.empty:
                working_df[col] = working_df[col].fillna(mode_value[0])
    
    # 3. UNIVERSAL TEXT CLEANING AND STANDARDIZATION
    for col in text_cols:
        working_df[col] = working_df[col].astype(str).str.strip().str.lower()
        
    # 4. UNIVERSAL OUTLIER CAPPING
    # Automatically cap all numeric columns at their 99th percentile
    for col in numeric_cols:
        cutoff = working_df[col].quantile(0.99)
        working_df[col] = working_df[col].clip(upper=cutoff)
        
    # 5. UNIVERSAL DUPLICATE/REDUNDANT COLUMN CLEANING
    # Drop rows that are completely empty across vital data
    working_df = working_df.dropna(how='all')
    
    return working_df


# ==========================================
# How to Run It in Production
# ==========================================

# 1. Load your raw data source
df_raw = sns.load_dataset('titanic')

# 2. Run the entire pipeline in exactly ONE line of code
df_clean = universal_clean_and_process(df_raw)

# 3. Inspect the clean output instantly
print("Pipeline successful! Current shape:", df_clean.shape)
print(df_clean.head(5))




# # ==========================================
# 6. Saving Clean Data to Files
# ==========================================

# 1. Save as a standard CSV file (Most Common)
# index=False prevents Pandas from creating an extra, unnamed row-number column
df_clean.to_csv('titanic_cleaned.csv', index=False)

# 2. Save as an Excel File (Requires the 'openpyxl' library installed)
df_clean.to_excel('titanic_report.xlsx', index=False, sheet_name='Cleaned Data')

# 3. Save as a JSON file (Great for web apps and APIs)
df_clean.to_json('titanic_data.json', orient='records', indent=4)

# 4. Save as a Parquet file (Best for huge datasets; saves storage space and loads fast)
df_clean.to_parquet('titanic_optimized.parquet', index=False)

print("All files exported successfully!")

# Critical Settings Explained index=False: By default, Pandas writes the row numbers (0, 1, 2, 3...) as the very first column in your new file. If you open it in Excel, you will see a messy column named Unnamed: 0. Setting index=False stops this from happening. orient='records': When saving to JSON, this option formats your data as a clean list of individual row blocks (e.g., [{"gender": "male", "age": 22}, {"gender": "female", "age": 38}]), which makes it easy for web developers to read.

# Where do these files go?By default, the files will be saved in the exact same folder where your Python script is currently running. If you want to save them somewhere specific, just provide the full path inside the quotes:
df_clean.to_csv('C:/Users/YourName/Documents/titanic_cleaned.csv', index=False)