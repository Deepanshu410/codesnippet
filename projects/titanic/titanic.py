import seaborn as sns
import matplotlib.pyplot as plt
df = sns.load_dataset('titanic')

df['age'] = df['age'].fillna(-1)

# 2. Handle text and categorical data safely
for col in ['embarked', 'deck', 'embark_town']:
    if df[col].dtype.name == 'category':
        # If it is a strict category, add 'Unknown' first
        df[col] = df[col].cat.add_categories('Unknown').fillna('Unknown')
    else:
        # If it is regular text, fill it directly
        df[col] = df[col].fillna('Unknown')

#print(df.isnull().sum())

#print(df)
sns.scatterplot(df, x='sex', y='age')
#plt.show()

print(df.head())