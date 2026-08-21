import pandas as pd

# Aggregate Functions, used to perform calculations on a set of values and return a single value as a result. Used to summarize and analyze data. Often used with the groupby() function to perform calculations on groups of data.

df = pd.read_csv('pokemon.csv')

# These aggregate functions would be applied to whole dataframe:
'''print(df.mean(numeric_only=True))  # Calculate the mean of all numeric columns
print(df.sum(numeric_only=True))  # Calculate the sum of all numeric columns
print(df.min(numeric_only=True))  # Calculate the minimum value of all numeric columns
print(df.max(numeric_only=True))  # Calculate the maximum value of all numeric columns
print(df.count())  # Count the number of non-null values in each column
print(df.median(numeric_only=True))  # Calculate the median of all numeric columns

# These functions would be applied to single column:
print(df['Height'].mean())  # Calculate the mean of the 'Height' column
print(df['Weight'].sum())  # Calculate the sum of the 'Weight' column
print(df['Weight'].min())  # Calculate the minimum value of the 'Weight' column
print(df['Weight'].max())  # Calculate the maximum value of the 'Weight' column
print(df['Type2'].count())  # Count the number of non-null values in the 'Type2' column'''

# groupby()
group = df.groupby('Type1')  # Group the DataFrame by the 'Type 1' column
print(group["Height"].mean())  # Calculate the mean of the 'Height' column for each group. Grouping each pokemon by their type and calculating the average height for each type.
print(group["Weight"].sum())  # Calculate the sum of the 'Weight' column for each group. Grouping each pokemon by their type and calculating the total weight for each type.
print(group["Weight"].min())  # Calculate the minimum value of the 'Weight' column for each group. Grouping each pokemon by their type and finding the lightest pokemon for each type.
print(group["Weight"].max())  # Calculate the maximum value of the 'Weight' column for each group. Grouping each pokemon by their type and finding the heaviest pokemon for each type.
print(group["Type2"].count())  # Count the number of non-null values in the 'Type2' column for each group. Grouping each pokemon by their type and counting how many pokemon of each type have a secondary type.
