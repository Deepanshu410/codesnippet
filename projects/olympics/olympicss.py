import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

'''# Generate 2026 Winter Olympics Medal Standings
np.random.seed(2026)
countries = ['Norway', 'Germany', 'United States', 'Canada', 'Austria', 
             'Sweden', 'Netherlands', 'Japan', 'Italy', 'Switzerland', 
             'France', 'South Korea', 'Finland', 'China', 'Slovenia']

data = {
    'Country': np.random.choice(countries, 150, p=[0.12, 0.10, 0.10, 0.09, 0.08, 0.07, 0.07, 0.06, 0.06, 0.05, 0.05, 0.05, 0.04, 0.03, 0.03]),
    'Sport': np.random.choice(['Biathlon', 'Alpine Skiing', 'Speed Skating', 'Figure Skating', 'Snowboard', 'Curling'], 150),
    'Medal_Type': np.random.choice(['Gold', 'Silver', 'Bronze', np.nan], 150, p=[0.25, 0.28, 0.32, 0.15])
}

df = pd.DataFrame(data)
# Add an ID column to represent individual athlete wins
df.insert(0, 'Athlete_ID', range(1001, 1001 + len(df)))
df.to_csv('olympics/olympics_2026.csv', index=False)
print("'olympics_2026.csv' has been generated successfully!")
'''
#  Task 1: Clean the MedalsLoad olympics_2026.csv. Check for missing values.The missing values in Medal_Type mean the athlete placed 4th or lower and didn't win a medal. Replace those specific NaN values with the string text "No Medal".
# 📊 Task 2: Count the WinsFind out how many total medals each country won.Hint: Instead of grouping and using .sum(), you will need to filter out the rows that say "No Medal", group by Country, and count how many rows are left using .size() or .count().
# 🎨 Task 3: Visualize the Sports DistributionCreate a Bar Chart showing how many athletes participated in each Sport.Hint: If you use Seaborn's sns.countplot(data=df, x='Sport'), it will automatically count the rows for you and build the bars without needing any extra Pandas math. Add your titles and axis labels.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Task 1: Clean
df = pd.read_csv('olympics/olympics_2026.csv')
df['Medal_Type'] = df['Medal_Type'].fillna("No Medal")

# Task 2: Count the Wins (The missing piece)
# 1. Filter out the rows where the athlete did not win a medal
medal_winners = df[df['Medal_Type'] != "No Medal"]

# 2. Group by Country and count how many rows (medals) each country has left
country_medal_counts = medal_winners.groupby('Country').size()

# 3. Print the results sorted from highest to lowest medal count
print(country_medal_counts.sort_values(ascending=False))


# Task 3: Visualize Sports Distribution
plt.figure(figsize=(10, 5))
sns.countplot(data=df, x="Sport", order=df['Sport'].value_counts().index)
plt.title("Athlete Participation by Sport")
plt.xlabel("Sport")
plt.ylabel("Number of Athletes")
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.show()
