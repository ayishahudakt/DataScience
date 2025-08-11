import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load the iris dataset
iris = load_iris()

# Sepal length is in column 0 of iris.data
sepal_length = iris.data[:, 0]

# Create histogram
plt.hist(sepal_length, bins=10, edgecolor='black')

# Labels and title
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")
plt.title("Histogram of Sepal Length (Iris Dataset)")

# Show plot
plt.show()

