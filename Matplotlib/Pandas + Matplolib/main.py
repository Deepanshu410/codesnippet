import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Pandas + Matplolib\pokemon.csv")
type_count = df["Type1"].value_counts(ascending=True)

# plot the quantity of each type. Put index(type name) on the y axis with a horizontal bar chart. Values(count of types) on the x axis


plt.barh(type_count.index, type_count.values, edgecolor='black')
plt.ylabel('Counts')
plt.xlabel('Types')
plt.title('Pokemon Type count distinction')
plt.tight_layout()
plt.show()

