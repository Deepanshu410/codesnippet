import pandas as pd

df = pd.read_csv('pokemon.csv')

# Filtering = keeping the rows that satisfy a condition and discarding the rest of the rows
# 1. Filtering rows by condition
tall_pokemon = df[df["Height"]>= 2]
heavy_pokemon = df[df["Weight"] > 100] 
legendary = df[df["Legendary"] == True]
water_pokemon = df[(df["Type1"] == "Water" ) | (df["Type2"] == "Water")] 
ff_pokemon = df[(df["Type1"] == "Fire" ) & (df["Type2"] == "Flying")] 
