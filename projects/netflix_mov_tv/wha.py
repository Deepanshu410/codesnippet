
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1: Loading file without UnicodeDecodeError by changing encoding from default to latin-1;
df = pd.read_csv("netflix_mov_tv\\netflix_titles.csv", encoding='latin-1')
#print(df)

# 2: Data Inspection;
print(f"Dataset contains; {df.shape[0]} rows and {df.shape[1]} coloumns.\n") # checks dataset dimensions (rows and columns)
#print(f"Missing values per coumn:\n {df.isnull().sum()}\n") # checks missing values in each column

# 3: Data Cleaning;
df['director'] = df['director'].fillna('Unknown') # filling missing text columns
df['cast'] = df['cast'].fillna('Unknown')
df['country'] = df['country'].fillna('Unknown')
df = df.dropna(subset=['date_added']) # for date added coloumn, drop it
#print(df.isnull().sum()) 

# 4: Data Types Standardization; Converting dates to system datetime objects
df['date_added'] = df['date_added'].str.strip() # strips accidental whitespace 
df['date_added'] = pd.to_datetime(df['date_added'], format='%B %d, %Y', errors='coerce') # converts to datetime format
df['year_added'] = df['date_added'].dt.year # Extracts the year netflix added the title to its platform

# 5: Data Visualization (Exploratory analysis); 
# Chart A: Distribution of content types
plt.figure(figsize=(6,4))
sns.countplot(x='type', data=df, palette='Reds_r')
plt.title('Netflix Catalog: Movies vs TV Shows')
plt.xlabel('Content Type')
plt.ylabel('Total Count')
plt.show()

# Chart B: Top 5 Content Exporting Countries
clean_countries = df[df['country'] != 'Unknown'] # filtering out 'Unknown' values filled earlier for a clean chart
plt.figure(figsize=(10,5))
sns.countplot(y='country', data=clean_countries, order=clean_countries['country'].value_counts().index[:5])
plt.show()































# Open the dataset safely by ignoring individual invisible broken bytes

'''# Verify it loaded by checking the row with 'Untold: Breaking Point'
print(df[df['show_id'] == 's102'])'''
'''
try:
    df = pd.read_csv('C:\programming files\projects\\netflix_mov_tv\\netflix_titles.csv', encoding='latin-1')
    file_path = 'C:\programming files\projects\\netflix_mov_tv\\netflix_titles.csv'
    with  open(file_path, "r") as file:
        content = csv.reader(file) # gives memory address, to access the data we need to iterate the data line by line
        for line in content:
            print(line[0]) #can access lines of data through index
except PermissionError:
    print("permission to this file is limited")
except UnicodeDecodeError:
    print("UnicodeDecodeError 2751")
'''


'''try: 
    with open(file_path, "a", newline="")as file:
        file.write(str(dict))
        print(f"text file '{file_path}' created")
except FileExistsError:
    print("file already exits")'''
