import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

'''np.random.seed(50)
n = 200
sectors = ['Finance', 'Healthcare', 'Tech', 'Government', 'Retail']
methods = ['Phishing', 'Ransomware', 'Malware', 'Insider Threat', np.nan]

data = {
    'Sector': np.random.choice(sectors, n, p=[0.25, 0.30, 0.20, 0.15, 0.10]),
    'Breach_Method': np.random.choice(methods, n, p=[0.40, 0.30, 0.15, 0.10, 0.05]),
    'Records_Stolen_Thousands': np.random.randint(5, 500, n)
}

df = pd.DataFrame(data)
df.to_csv('cyberbreaches/cyber_breaches.csv', index=False)
print("'cyber_breaches.csv' has been generated successfully!")
'''

# 🛠️ Task 1: Clean the Breach MethodsLoad cyber_breaches.csv.Check for missing values.Replace any missing NaN values in the Breach_Method column with the text string "Unknown".
# 📊 Task 2: Filter and Total (Combining patterns!)We want to see the total number of records stolen, but only for the Healthcare sector.Hint 1: First, filter your rows to keep only healthcare entries: healthcare_df = df[df['Sector'] == 'Healthcare'].Hint 2: Then, select the Records_Stolen_Thousands column from that new dataset and use .sum(). Print the total.
# 🎨 Task 3: Visualize the Breach MethodsUse Seaborn's sns.countplot() to show how frequently each Breach_Method occurs across the whole dataset.Add your title and labels using Matplotlib.

df = pd.read_csv('cyberbreaches/cyber_breaches.csv')
print(df.isnull().sum())
df['Breach_Method'] = df['Breach_Method'].fillna("Unknown")
healthcare_df = df[df['Sector'] == 'Healthcare']
print(healthcare_df['Records_Stolen_Thousands'].sum())
sns.countplot(data=df, x='Breach_Method')
plt.xlabel('Breach Methods')
plt.title('Breach Methods Occurences')
plt.show()