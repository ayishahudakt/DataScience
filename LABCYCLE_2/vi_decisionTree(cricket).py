# cricket_c50.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt

# Step 1: Load dataset
data = pd.read_csv("cricket.csv")

# Step 2: Separate features and target
X = data.iloc[:, :-1]   # All columns except last
y = data.iloc[:, -1]    # Last column is target (Play: Yes/No)

# Step 3: Encode categorical data if needed
X = pd.get_dummies(X)
y = y.map({'Yes': 1, 'No': 0})  # optional (depends on dataset labels)

# Step 4: Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Step 5: Build Decision Tree (C5.0 equivalent)
# criterion='entropy' => ID3/C4.5/C5.0 style
model = DecisionTreeClassifier(criterion='entropy', random_state=42)
model.fit(X_train, y_train)

# Step 6: Make predictions
y_pred = model.predict(X_test)

# Step 7: Evaluate performance
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Step 8: Visualize the tree
plt.figure(figsize=(12,6))
plot_tree(model, filled=True, feature_names=X.columns, class_names=['No', 'Yes'])
plt.title("C5.0 Decision Tree for Cricket Play Prediction")
plt.show()
