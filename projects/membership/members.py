import numpy as np
import pandas as pd

np.random.seed(101)
data = {
    "Customer_ID": [f"CUST_{i}" for i in range(1, 201)],
    "Age": np.random.randint(18, 70, 200).astype(float),
    "Membership_Type": np.random.choice(["Basic", "Premium", "VIP"], 200),
    "Monthly_Spend": np.random.randint(20, 150, 200).astype(float),
    "Churned": np.random.choice([0, 1], 200, p=[0.7, 0.3]),
}
df_ml = pd.DataFrame(data)

# Introduce missing data
df_ml.loc[np.random.choice(df_ml.index, 15, replace=False), "Age"] = np.nan
df_ml.loc[np.random.choice(df_ml.index, 10, replace=False), "Monthly_Spend"] = np.nan


#You Need Next To transition seamlessly into machine learning, add these four specific techniques to your practice routine:df.drop(): Models cannot use columns like Flight_ID or Passenger_Name because unique identifiers contain no patterns. You must learn to drop irrelevant features.pd.get_dummies(): This converts text columns (categorical data) into numbers (0s and 1s). This process is called One-Hot Encoding, and it is mandatory for text columns in Scikit-Learn..value_counts(): Before modeling, you must know how your data is distributed. This function instantly counts how many rows belong to each category.df.corr(numeric_only=True): This builds a correlation matrix. It shows you exactly which numbers have a strong relationship with your target variable, helping you choose the best features for your model.

# Your Action Items
# Inspect: Use .value_counts() on the Churned column to see how many customers actually left.
# Impute: Fill missing values in Age with the median age, and missing values in Monthly_Spend with the mean spend. (Hint: Look up df['Col'].median() and df['Col'].mean()).
# Drop: Remove the Customer_ID column entirely since a machine learning model cannot use text IDs.
# Encode: Convert the Membership_Type column into numerical columns using pd.get_dummies().

# 1. inspection & imputation
print(df_ml["Churned"].value_counts())
df_ml["Age"] = df_ml["Age"].fillna(df_ml["Age"].median())
df_ml["Monthly_Spend"] = df_ml["Monthly_Spend"].fillna(df_ml["Monthly_Spend"].mean())

# 2. Drop the column and specify it's a column (axis=1), then save it back
df_ml = df_ml.drop("Customer_ID", axis=1)

# 3. Run get_dummies and overwrite the DataFrame with the fully numeric version
df_final = pd.get_dummies(df_ml, columns=["Membership_Type"], drop_first=True, dtype=int)

# Inspect the ready-to-use dataset
print(df_final.head())
