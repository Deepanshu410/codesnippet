from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV

# 1. DATA ACQUISITION
# Loads the raw features (X) and category labels (y) directly as NumPy arrays.
X, y = load_iris(return_X_y=True) # return_X_y=True strips all that is not numerical
# X stores continuous measurements (decimals). These are the physical dimensions of each flower's petals and sepals (e.g., 5.1, 3.5, 1.4, 0.2).
#y stores categorical codes (integers). It uses numbers strictly as nicknames for the flower names. Instead of writing text like "Setosa", it stores a 0, 1, or 2

#Scikit-Learn Target Encoding (X vs y) In scikit-learn, the target array y uses Label Encoding (integers like 0, 1, 2) rather than One-Hot Encoding. While label encoding is generally bad for unordered features in X (as algorithms mistakenly treat them as numerical rankings like \(2 > 1 > 0\)), it is perfectly safe for the target y. This is because classification algorithms treat y values strictly as symbolic "bucket labels" or group identities to group the features, rather than performing mathematical operations (like addition or averaging) on them. Additionally, while the categories themselves are unordered, the raw load_iris dataset is block-ordered (all 0s, then all 1s, then all 2s), making it crucial to shuffle the data before training to ensure proper model learning.

# 2. DATA SPLITTING
# Splits data: 80% for training the model, 20% held back to test its accuracy.
# random_state=1 ensures you get the exact same split every time you run it.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# 3. FEATURE SCALING (PREPROCESSING)
# Initializes the scaler to standardize features (mean=0, variance=1). variance meaning something varies by some value. 
# How StandardScaler Uses Mean and Variance: Mean = 0 (Centering): Centralises the entire dataset around 0, which represents the exact average. This shifts the data so that any value below average automatically becomes a negative number, while any value above average becomes a positive number. Variance = 1 (Scaling): Performs two critical functions. First, it eliminates and flattens the original physical units (like dollars or years) to prevent scale confusion and data disparity between features. Second, it physically shrinks wildly spread-out data or stretches tightly packed data so that all features fit into a uniform, standardized thickness.
scaler = StandardScaler()

# Fits the scaler to learn training data patterns AND transforms the training data.
X_train_scaled = scaler.fit_transform(X_train)

# ONLY & ALWAYS transforms the test data using the training data's learned patterns.
# This prevents "data leakage" from the test set into your model.
X_test_scaled = scaler.transform(X_test)


'''
In scikit-learn, a dataset is structured into features (X) and target labels (y). X contains the independent numerical or categorical variables, while y represents the dependent target variable or group identifiers we want to predict. For classification tasks like load_iris, y uses integer numbers (label encoding) as simple group tags to organize the data into distinct buckets without performing mathematical operations between them (which is why label encoding is used here even though the features are unordered). To prevent metadata and documentation from loading, the return_X_y=True parameter acts as a quick shortcut to return just the clean arrays.

Next, the data is split into four parts using train_test_split: X_train, X_test, y_train, and y_test, ideally using an 80-20 or 70-30 split. The random_state parameter acts as a static seed to ensure the exact same split occurs every time the code runs.

During preprocessing, StandardScaler() initializes a scaler to standardize features (mean=0, variance=1). Calling fit_transform(X_train) calculates the training set's unique mean and variance to scale X_train, forcing its resulting mean to 0 and variance to 1. This step establishes a single, universal "ruler" based strictly on the training data. Finally, we only call transform(X_test) on the test data. This forces the test set to be scaled using the training data's saved parameters rather than creating a second, conflicting ruler. Keeping this single reference point ensures that identical scaled numbers mean the exact same thing to the machine learning model during both training and evaluation, completely avoiding train-test distribution contamination.

'''
# 4. MODEL CREATION & TRAINING (CLASSIFICATION)
# Initializes the **classification model** (Logistic Regression).
reg = LogisticRegression()

# Trains the model by letting it learn the relationship between scaled features and labels.
reg.fit(X_train_scaled, y_train)

# 5. MODEL EVALUATION (ACCURACY)
# Calculates classification accuracy (percentage of correct guesses) on unseen test data.
# Note: For classification, this returns Accuracy, not an R² score.
reg.score(X_test_scaled, y_test)

# 6. INDIVIDUAL PREDICTION
# Extracts the very first flower's scaled features from the test set.
single_instance = X_test_scaled[0]

# Predicts the class (0, 1, or 2) for this single flower. Expects a 2D array [[]].
print(reg.predict([single_instance]))

# 7. BULK PREDICTION & DIAGNOSTICS
# Generates predictions for all 30 flowers in the scaled test set. test_size=0.2, which is 20% of 150(total flowers)
y_pred = reg.predict(X_test_scaled)

'''
Once the data is preprocessed, model training begins by initializing an algorithm like LogisticRegression(), which despite its name, is a classification model used to categorize data into discrete groups. Upon initialization, the model sets up internal parameters called weights (coefficients for each feature column that dictate their importance and direction) and a single bias (the baseline intercept or default assumption). These parameters start as zeros or arbitrary numbers.

When reg.fit(X_train_scaled, y_train) is executed, the model replaces these initial placeholders with optimized values through a trial-and-error mathematical loop called Gradient Descent. The model reviews each row of X_train_scaled, calculates a probability guess using its current parameters, and evaluates its accuracy against the true answer key in y_train. If its prediction is off, it mathematically calculates the error and adjusts both the weights and the bias—increasing the weights of features heavily linked to the correct outcome. This iterative correction continues across the entire training set until the model finds the optimal decision boundary, permanently saving the final coefficients in reg.coef_ and the intercept in reg.intercept_. Having the features standardized beforehand (mean=0, variance=1) is crucial here, as it ensures all inputs sit on a level playing field, preventing large-scale features from dominating and distorting the parameter adjustment process. Finally, reg.score(X_test_scaled, y_test) uses these fixed weights and bias to make predictions on the unseen test data and returns the final classification accuracy.
'''

# Generates a grid comparing actual classes (rows) vs predicted classes (columns).
# Useful for seeing exactly which flower types the model misclassified.
print(confusion_matrix(y_test, y_pred)) # Rows represent the Actual classes (0, 1, and 2). Columns represent the Predicted classes (0, 1, and 2).
# Model's Performance Breakdown; Class 0 (Setosa): 11 flowers were actually Setosa, and your model guessed all 11 correctly. Perfect!Class 1 (Versicolor): 13 flowers were actually Versicolor. The model got 12 right, but misclassified 1 flower as Class 2 (Virginica).Class 2 (Virginica): 6 flowers were actually Virginica, and the model got all 6 right.



# --- 1. THE ASSEMBLY LINE (PIPELINE) ---
# Glue preprocessing (scaler) and the model together into a single automated workflow
pipe = Pipeline([
    ('scaler', StandardScaler()),       # Step 1: Standardize features to mean=0, variance=1
    ('model', LogisticRegression())     # Step 2: Classification model to predict categories
])

# --- 2. TRAINING AND TESTING VIA THE PIPELINE ---
# Automatically fit the scaler and train the model using raw training data in one go
pipe.fit(X_train, y_train)

# Automatically scale raw X_test using training rules and calculate final classification accuracy
accuracy = pipe.score(X_test, y_test)
print(f"Pipeline Accuracy: {accuracy}")

# Grab the first raw flower from the test set (maintaining 2D shape [[]])
raw_instance = X_test[0]

# Pass raw data directly; pipeline handles scaling internally before generating the prediction
prediction = pipe.predict([raw_instance])
print(f"Pipeline Prediction: {prediction}")


# --- 3. MULTI-EXAM ROTATION (CROSS-VALIDATION) ---
# Rotate through the entire dataset in 5 distinct splits to get a realistic performance average
scores = cross_val_score(pipe, X, y, cv=5)

print("All 5 scores:", scores)
print("Average Accuracy:", scores.mean())


# --- 4. TUNING THE KNOBS (GRID SEARCH) ---
# Define dictionary of hyperparameter settings; 'model__C' targets the 'model' step inside the pipeline
param_grid = {
    'model__C': [0.1, 1.0, 10.0, 100.0]
}

# Combine pipeline, parameter grid, and 5-fold cross-validation into an automated search agent
grid_search = GridSearchCV(pipe, param_grid, cv=5)

# Execute the grid search across all combinations to locate the optimal configuration
grid_search.fit(X, y)

# Output the single best-performing parameter setting and its corresponding accuracy score
print("Best Settings:", grid_search.best_params_)
print("Best Accuracy Score:", grid_search.best_score_)


from sklearn.ensemble import RandomForestClassifier
