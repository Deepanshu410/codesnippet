import kagglehub
import pandas as pd
import numpy as np


'''# Download latest version
path = kagglehub.dataset_download("brendan45774/test-file")

print("Path to dataset files:", path)'''

ds = pd.read_csv("C:\\Users\\vidya\\.cache\\kagglehub\\datasets\\brendan45774\\test-file\\versions\\6\\tested.csv")
ds['Age'] == ds['Age'].fillna(ds['Age'].mean())
ds['Fare'] == ds['Fare'].fillna(ds['Fare'].mean())
ds['Cabin'] == ds['Cabin'].fillna('NaN')
print(ds.isnull().sum())