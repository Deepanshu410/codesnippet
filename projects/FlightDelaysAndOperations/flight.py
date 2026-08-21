import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Seed for reproducibility
np.random.seed(42)

# Generate realistic flight data
data = {
    "Flight_ID": [f"FL{i}" for i in range(1001, 1201)],
    "Airline": np.random.choice(
        ["SkyLink", "DeltaJet", "EcoAir", "StarFly"], 200
    ),
    "Destination": np.random.choice(
        ["New York", "London", "Tokyo", "Paris", "Chicago"], 200
    ),
    "Status": np.random.choice(
        ["On-Time", "Delayed", "Cancelled", "Delayed"], 200, p=[0.6, 0.2, 0.05, 0.15]
    ),
    "Delay_Minutes": np.random.randint(15, 120, 200).astype(float),
    "Passengers_Booked": np.random.randint(80, 250, 200),
}

df = pd.DataFrame(data)

# Introduce realistic missing data and anomalies
df.loc[df["Status"] == "On-Time", "Delay_Minutes"] = (
    np.nan
)  # On-time flights have NaN delay
df.loc[df["Status"] == "Cancelled", "Delay_Minutes"] = (
    np.nan
)  # Cancelled flights have NaN delay
df.loc[df["Status"] == "Cancelled", "Passengers_Booked"] = (
    0  # No passengers flown
)

# Randomly insert missing values into 'Status' to simulate human error
df.loc[np.random.choice(df.index, 12, replace=False), "Status"] = np.nan

# The 3-Task Challenge
# Task 1: Clean, Locate, and count all missing values in the Status column. Replace those specific missing Status values with the string "Unknown".For any remaining missing values in Delay_Minutes, fill them with 0.
# Task 2: Analyze, Filter the dataset to look only at flights going to "Tokyo".Using this filtered data, group by the airline.Calculate the total (sum) number of passengers booked for each airline heading to Tokyo.
# Task 3: VisualizeCreate a single figure containing a 1-row, 2-column subplot structure using Matplotlib. Plot 1 (Left): Build a bar plot showing the total total delay minutes for each unique flight status.Plot 2 (Right): Build a bar plot showing the total delay minutes for each airline.Constraint: Use Seaborn for the bar plots and ensure your bars represent the total sum of delays, not the average.

print(df.isnull().sum())
df['Status'] = df["Status"].fillna("Unknown")
df['Delay_Minutes'] = df["Delay_Minutes"].fillna(0)
tokyo = df[df['Destination'] == 'Tokyo']
airlines = tokyo.groupby('Airline')['Passengers_Booked'].sum()

# 1. Create the blank Matplotlib canvas (1 row, 2 columns)
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# 2. Tell Seaborn to draw the first barplot on axes[0] (Left)
sns.barplot(data=df, x="Status", y="Delay_Minutes", estimator=sum, ax=axes[0])

# 3. Tell Seaborn to draw the second barplot on axes[1] (Right)
sns.barplot(data=df, x="Airline", y="Delay_Minutes", estimator=sum, ax=axes[1])
plt.tight_layout()             
plt.show()