import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

# Step 1: Load the dataset
data = pd.read_csv("person.csv")

# Step 2: Separate features (X) and target (y)
# Assume the last column is the target (Cheat/NoCheat)
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

# Step 3: Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Step 4: Create Decision Tree model (C5.0 uses entropy as criterion)
model = DecisionTreeClassifier(criterion="entropy", random_state=42)

# Step 5: Train the model
model.fit(X_train, y_train)

# Step 6: Make predictions
y_pred = model.predict(X_test)

# Step 7: Evaluate model performance
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Step 8: Predict for new data (optional)
# Example: new_person = [[feature1, feature2, feature3, feature4, feature5]]
# print("Predicted class:", model.predict(new_person)[0])
