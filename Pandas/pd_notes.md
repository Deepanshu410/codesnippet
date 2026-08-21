###### INTRO:

Pandas(panel data): widely used in data analysis, ds, and ml. Using this we **work with objects known as Series and DataFrames.**

A series is a one-dimensional labeled coloumn. A DataFrame is a two-dimensional labeled grid of table. 

Using this library we can **import, display, manipulate, and export tabular data.**



###### Topics needed: 

variables, user input, math, logical operators, comparison operators, lists, tuples, sets



###### **SERIES:**

Series, a Pandas 1-dimensional labeled array that can hold any data type. It's like a single coloumn in a spreadsheet (1-dimensional). 

\- .loc\[] to **access** a group of rows and columns **by labels**

\- .iloc\[2] **location by integer** iloc (integer location)

\- pd.Series(calories) # **creates a Series object** from the given dictionary.



###### **DATA FRAME:**

DataFrame, a tabluar structure with rows and coloumns. (2 dimensional). Similar to an Excel spreadsheet.

DataFrame is a constructor that creates a DataFrame object from the provided data. It takes a dictionary where the keys are column names and the values are lists of column data.

\- df\['Occupation'] = \['Engineer', 'Doctor', 'Artist', 'Lawyer'] , **adding a new column** to the DataFrame

\- **adding a new row** to the DataFrame;

&#x20;   new\_row = pd.DataFrame(\[{'Name': 'Eve', 'Age': 28, 'City': 'Miami', 'Occupation': 'Designer'},

&#x20;                      {'Name': 'Steve', 'Age': 29, 'City': 'Seattle', 'Occupation': 'Teacher'}], index=\['E', 'F']) 

\- pd.concat(\[df, new\_row]) , **to concatenate two DataFrames** along a particular axis. In this case, we are concatenating the existing DataFrame df with the new\_row DataFrame along the rows (axis=0)



###### **IMPORTING \& SELECTION:**

\- print(df) , **with truncation**

\- print(df.to\_string()) , **without truncation**

\- **eg.** df\[\['Name', 'Type 1']], df.loc\['Bulbasaur'], df.iloc\[0:10:2, 0:3], etc.





###### **FILTERING:**

Filtering = **keeping the rows that satisfy a condition** and discarding the rest of the rows

\- **eg.** heavy\_pokemon = df\[df\["Weight"] > 100] 



###### **AGGREGATION:** **(mean, min, max, sum, count, etc.)**

Aggregate Functions, used to perform calculations on a set of values and return a single value as a result. Used to summarize and analyze data. Often used with the **groupby()** function to perform calculations on groups of data.



###### **Data Cleaning:**

Is the process of fixing or removing incorrect, corrupted, incorrectly formatted, duplicate, or incomplete data within a dataset. Approximately 75% of work done with Pandas is data cleaning.

\- dropna() for **removing**, fillna() for **replacing**/ alternative .replace() for replacing more data with one line of code

\- .astype(bool) for **changing datatypes**, drop\_duplicates() for **removing duplicates**



