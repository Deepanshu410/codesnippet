# when the dataset does not have much numercial data to feed, we need to convert the numerical data in oder to feed it to the model.

from sklearn.datasets import fetch_openml # fetch_openml: A helper function to download public datasets directly from the OpenML platform.
from sklearn.preprocessing import OrdinalEncoder

data = fetch_openml('car', as_frame=True).frame # as_frame=True: Tells the function to return the data as a pandas DataFrame instead of a raw NumPy array.
# .frame: Extracts the actual table structure containing both features and targets.
columns_to_encode = ['lug_boot', 'safety']
encoder = OrdinalEncoder(
    categories= [
        ['small', 'med', 'big'],
        ['low', 'med', 'high']
    ]
)
data[columns_to_encode] = encoder.fit_transform(data[columns_to_encode]) # fit_transform(): Does two jobs at once. fit learns: It looks at your custom list and learns: small = 0, med = 1, big = 2.transform applies: It replaces the text directly inside the existing columns. It does not create new columns.
# data[columns_to_encode] = ...: Overwrites the original text columns with the new numeric columns in your DataFrame.
#print(data)

#encoder.inverse_transform(data[columns_to_encode]) # inverse_transform(): Converts the numbers back into the original text string categories. Useful for analyzing model predictions later.

## to convert values of broad spectrum; (one-hot)
import pandas as pd
from sklearn.datasets import fetch_openml  # Added missing import
from sklearn.preprocessing import OneHotEncoder

# 1. Fetch titanic dataset
data = fetch_openml("titanic", version=1, as_frame=True).frame

# 2. counting occurrences of different sex
print(data.sex.value_counts())

encoder = OneHotEncoder(handle_unknown="ignore", sparse_output=False) 
# handle_unknown="ignore": If the model encounters a brand new category in future test data, it won't crash; it will just give it all zeros.
# sparse_output=False: Forces the tool to output a readable NumPy array instead of a compressed matrix format.

# 3. Use double brackets [[...]] for selecting multiple columns
encoded_values = encoder.fit_transform(data[["sex", "embarked"]]) 
# fit learns: It looks at the text and counts the unique values (e.g., male and female).transform applies: It explodes the text into a completely new binary grid of 1s and 0s.
# [["sex", "embarked"]]: Double brackets are required because scikit-learn encoders expect a 2D table input (rows and columns), not a 1D list series.
# encoded_values: Holds a raw matrix of 1s and 0s.
new_cols = encoder.get_feature_names_out(["sex", "embarked"])
# get_feature_names_out(): Dynamically generates the new column headers. For example, if "sex" has male and female, it creates labels like sex_male and sex_female.

print(encoded_values)
print(new_cols)

df_encoded = pd.DataFrame(encoded_values, columns=new_cols, index=data.index)
# pd.DataFrame(...): Converts the raw NumPy matrix back into a formatted pandas DataFrame. doing this again because creating new columns by new_cols, the data is in raw numpy matrix. 
# index=data.index: copies the row numbers from your original dataset to make sure the rows line up perfectly when combined later.

# 4. Drop the columns we encoded and concat the new ones
data_final = pd.concat(
    [data.drop(columns=["sex", "embarked"]), df_encoded], axis=1
)
# data.drop(columns=["sex", "embarked"])This temporarily creates a copy of your original dataset but deletes the text columns. We do this because if we leave the raw text columns in the final data, the machine learning model will crash.
# concat is short for concatenate (to link things together). axis=1 explicitly tells Python to glue them together side-by-side (horizontally) like columns, rather than stacked on top of each other like rows.
print(data_final)
