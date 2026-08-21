import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'], 
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
df = pd.DataFrame(data, index=['A', 'B', 'C', 'D']) # DataFrame is a constructor that creates a DataFrame object from the provided data. It takes a dictionary where the keys are column names and the values are lists of column data. The resulting DataFrame will have columns 'Name', 'Age', and 'City' with the corresponding data from the lists.
print(df)

# loc and iloc are also used in DataFrames with the same functionality as in Series, but they operate on the DataFrame's rows and columns. 

# adding a new column to the DataFrame: 
df['Occupation'] = ['Engineer', 'Doctor', 'Artist', 'Lawyer']

# adding a new row to the DataFrame:
new_row = pd.DataFrame([{'Name': 'Eve', 'Age': 28, 'City': 'Miami', 'Occupation': 'Designer'},
                       {'Name': 'Steve', 'Age': 29, 'City': 'Seattle', 'Occupation': 'Teacher'}], index=['E', 'F'])
df = pd.concat([df, new_row]) # The concat function is used to concatenate two DataFrames along a particular axis. In this case, we are concatenating the existing DataFrame df with the new_row DataFrame along the rows (axis=0). pd.append is another method that can be used to add a new row to a DataFrame, but it is deprecated in recent versions of pandas. 
print(df)