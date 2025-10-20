import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier

# Step 1: Read dataset from CSV file
data = pd.read_csv("food_data.csv")

# Step 2: Separate features and labels
X = data[['Sweetness', 'Crunchiness']].values
y = data['Label'].values

# Step 3: Normalize features using Min-Max Scaler
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# Step 4: Create and train the KNN classifier
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_scaled, y)

# Step 5: Classify new food item - Carrot (sweetness=2, crunchiness=8)
new_item = [[2, 8]]
new_item_scaled = scaler.transform(new_item)

# Step 6: Predict the class
prediction = knn.predict(new_item_scaled)

print("New food item: Carrot")
print("Sweetness: 2, Crunchiness: 8")
print("Predicted Class:", prediction[0])
