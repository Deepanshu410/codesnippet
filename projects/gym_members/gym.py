import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

'''np.random.seed(10)
n = 300
data = {
    'Age': np.random.randint(18, 65, n),
    'Workout_Type': np.random.choice(['Cardio', 'Strength', 'Yoga', 'HIIT'], n),
    'Session_Duration_Min': np.random.randint(30, 120, n),
    'Calories_Burned': np.random.choice([np.nan, 250, 400, 600, 750], n, p=[0.05, 0.25, 0.25, 0.25, 0.20])
}
df = pd.DataFrame(data)
# Add some realistic variance to calories based on duration
df['Calories_Burned'] = df['Calories_Burned'].fillna(df['Session_Duration_Min'] * 6)
df.loc[np.random.choice(n, 15, replace=False), 'Calories_Burned'] = np.nan
df.to_csv('gym_members/gym_members.csv', index=False)
print("'gym_members.csv' created. Training wheels are officially off.")
'''
# Clean: Load gym_members.csv. Check for missing values, and fill any missing values in the Calories_Burned column with 0.
# Analyze: Find the average (.mean()) session duration grouped by each Workout_Type.
# Visualize: Create a scatter plot showing Age on the X-axis and Calories_Burned on the Y-axis. Give it a title.

df = pd.read_csv('gym_members/gym_members.csv')
print(df.describe())
print(df.info())
print(df.isnull().sum()) #
df['Calories_Burned'] = df['Calories_Burned'].fillna(0) #
group = df.groupby('Workout_Type') #
print(f"average session duration grouped by each Workout_Type: {group['Session_Duration_Min'].mean()}")

plt.scatter(data=df, x="Age", y="Calories_Burned")
plt.title("Workout measurement")
plt.xlabel("Age")
plt.ylabel("Calories Burned")
plt.show()
