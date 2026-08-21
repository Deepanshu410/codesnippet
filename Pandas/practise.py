import pandas as pd 

# importing and selecting data: have a user type int he name of a pokemon and return all the data for that pokemon (the row with the index of the pokemon name)
df = pd.read_csv('pokemon.csv')
pokeman = input("Enter the name of a pokemon: ")

try:
    print(df.loc[pokeman])
except KeyError:
    print(f"Pokemon '{pokeman}' not found. Please check the spelling and try again.")