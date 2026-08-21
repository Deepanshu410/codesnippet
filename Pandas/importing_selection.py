import pandas as pd
df = pd.read_csv('pokemon.csv', index_col="Name") # this will set the 'Name' column as the index of the dataframe
print(df) # with truncation
print(df.to_string()) # to print all the data in the dataframe without truncation (shortening something by cutting off a part of it, usually the end)


# for json
# df = pd.read_json('pokemon.json')

# SELECTION: 
# 1. Selecting a column
print(df['Name']) # this will return a series (a single column of data)
# 2. Selecting multiple columns
print(df[['Name', 'Type 1']]) # this will return a dataframe (multiple columns of data)
# 3. Selecting rows by index
print(df.iloc[0:10:2, 0:3]) # this will return the first 10 rows of the dataframe, but only every 2nd row (0, 2, 4, 6, 8) and only the first 3 columns (0, 1, 2)
# 3.1. Selecting rows by label    
print(df.loc['Bulbasaur']) # this will return the row with the index 'Bulbasaur'
print(df.loc['Charizard', ["Height", "Weight"]]) # this will return the 'Height' and 'Weight' columns for the row with the index 'Charizard'
print(df.loc['Bulbasaur':'Charmander' ]) # this will return all the rows from 'Bulbasaur' to 'Charmander' (inclusive)
# 4. Selecting rows by condition
print(df[df['Type 1'] == 'Fire']) # this will return all the rows where the 'Type 1' column is equal to 'Fire'
# 5. Selecting rows and columns
print(df.loc[0:5, ['Name', 'Type 1']]) # this will return the first 5 rows of the 'Name' and 'Type 1' columns
# 6. Selecting rows and columns by condition    
print(df.loc[df['Type 1'] == 'Fire', ['Name', 'Type 1']]) # this will return all the rows where the 'Type 1' column is equal to 'Fire' and only the 'Name' and 'Type 1' columns
# 7. Selecting rows and columns by condition with multiple conditions
print(df.loc[(df['Type 1'] == 'Fire') & (df['Type 2'] == 'Flying'), ['Name', 'Type 1', 'Type 2']]) # this will return all the rows where the 'Type 1' column is equal to 'Fire' and the 'Type 2' column is equal to 'Flying' and only the 'Name', 'Type 1', and 'Type 2' columns

