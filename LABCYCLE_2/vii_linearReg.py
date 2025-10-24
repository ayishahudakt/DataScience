# Import necessary libraries
import pandas as pd
from sklearn.linear_model import LinearRegression

# Step 1: Read the CSV file (tab-separated)
heart = pd.read_csv("heart.csv", sep=r"\s+")

# Step 2: Display the first few rows to confirm correct columns
print("Dataset preview:\n", heart.head())

# Step 3: Split the dataset into training and testing data
heart_train = heart.iloc[:400]   # First 400 rows for training
heart_test = heart.iloc[400:]    # Remaining rows for testing

# Step 4: Define independent (X) and dependent (y) variables
X_train = heart_train[['biking', 'smoking']]     # Independent variables
y_train = heart_train['heart.disease']           # Dependent variable

X_test = heart_test[['biking', 'smoking']]
y_test = heart_test['heart.disease']

# Step 5: Create and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 6: Display regression coefficients
print("\nRegression Coefficients:", model.coef_)
print("Intercept:", model.intercept_)

# Step 7: Predict on test data
y_pred = model.predict(X_test)

print("\nPredicted values:")
print(y_pred)


