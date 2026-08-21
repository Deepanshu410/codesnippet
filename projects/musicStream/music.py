import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

'''np.random.seed(99)
n = 250
genres = ['Rock', 'Pop', 'Hip-Hop', 'Jazz', 'Electronic']
explicit_options = ['Yes', 'No', np.nan]

data = {
    'Track_Name': [f'Track_{i}' for i in range(1, n+1)],
    'Genre': np.random.choice(genres, n, p=[0.20, 0.35, 0.25, 0.10, 0.10]),
    'Streams_Millions': np.random.randint(1, 150, n),
    'Explicit_Content': np.random.choice(explicit_options, n, p=[0.15, 0.80, 0.05])
}

df = pd.DataFrame(data)
df.to_csv('musicStream/music_streaming.csv', index=False)
print("'music_streaming.csv' has been generated. The floor is yours.")
'''

# 🛠️ Task 1: CleanLoad music_streaming.csv.Find the missing data.Replace any missing value in the Explicit_Content column with the string text "Unknown".
# 📊 Task 2: Filter & AnalyzeThe business wants to check the performance of Hip-Hop music.Filter the dataset to isolate only tracks where the Genre is exactly "Hip-Hop".Calculate and print the average (.mean()) number of streams (Streams_Millions) for those Hip-Hop tracks.
# 🎨 Task 3: VisualizeCreate a chart showing the total number of streams for each Genre.Hint: Since you want to add up a numeric column (Streams_Millions) across categories (Genre), a standard Seaborn countplot won't work on its own. Instead, look at your notes from your Superstore Sales project to see how we used sns.barplot with estimator=sum.Add a title, X-axis label, and Y-axis label.

df = pd.read_csv('musicStream/music_streaming.csv')
df['Explicit_Content'] = df['Explicit_Content'].fillna("Unknown")
print(df.isnull().sum())
hip_hop = df[df['Genre'] == 'Hip-Hop']
print(hip_hop)
avg_Stream_num = hip_hop['Streams_Millions'].mean()
print(avg_Stream_num)

sns.barplot(data=df, x='Genre', y='Streams_Millions', estimator=sum, errorbar=None)
plt.xlabel('Genre')
plt.ylabel('Streams (Millions)')
plt.title('Total Streams by Genre')
plt.show()

