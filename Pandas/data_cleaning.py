import pandas as pd

# data cleaning, is the process of fixing or removing incorrect, corrupted, incorrectly formatted, duplicate, or incomplete data within a dataset. It is an essential step in the data analysis process, as it ensures that the data is accurate and reliable for analysis.Approximately 75% of work done with Pandas is data cleaning. 

df = pd.read_csv('pokemon.csv')

# drop/remove irrelevant columns:
# df = df.drop(columns = ["Legendary", "No"]) 

# handling missing data:
df = df.dropna(subset=["Type2"]) # drop rows with missing type2 values

# replacing missing values with a specific value:
df = df.fillna({"Type2": "None"}) # replace missing type2 values with "None"

# fixing any inconsistent values:
df["Type1"] = df["Type1"].replace({"Grass": "GRASS",
                                   "Fire": "FIRE"}) 

# standardize text 
df["Name"] = df["Name"].str.lower()

# fix or changing data types:
df["Legendary"] = df["Legendary"].astype(bool) # convert Legendary column to boolean

# removing duplicates:
df = df.drop_duplicates() # remove duplicate rows