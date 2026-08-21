import pandas as pd
data = [100, 103,105, 107, 110]
series = pd.Series(data, index=['A', 'B', 'C', 'D', 'E']) # pd.Series() is used to create a Series object from the given data list. It's a constructor method, not a function that takes the data and converts it into a Series format. The resulting Series will have an index automatically assigned to each element, starting from 0 unless specified otherwise. Along with the index, there'll be metadata (dtype) associated with the Series, which indicates the type of data it contains (in this case, integers).
print(series.loc['C']) # location by label or loc (location) is used to access a group of rows and columns by labels or a boolean array. The output will include the values corresponding to labels 'A', 'B', and 'C'.
series.loc["C"] = 106 # updates the value at index 'C' to 106. 
print(series.iloc[2]) # location by integer iloc (integer location) is used to access a value by integer position(s).

# filtering: 
print(series[series > 105])

# Dictionary instead of list:
calories = {'A': 2000, 'B': 2200, 'C': 1900, 'D': 2500, 'E': 3000}
series.loc['C'] = 2050 # updates to 2050.
series1 = pd.Series(calories) # creates a Series object from the given dictionary. The keys of the dictionary will become the index of the Series, and the values will become the data of the Series.
print(series1[series1 >= 2000]) # days with consumed 2000 or more calories.