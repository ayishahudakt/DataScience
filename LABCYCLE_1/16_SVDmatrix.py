import numpy as np

# Step 1: Input order of the square matrix
n = int(input("Enter the order (n) of the square matrix: "))

# Step 2: Input matrix elements
print(f"Enter the elements of the {n}x{n} matrix row-wise:")
matrix = []
for i in range(n):
    row = list(map(float, input().split()))
    matrix.append(row)

A = np.array(matrix)

# Step 3: Perform SVD
U, S, VT = np.linalg.svd(A)

# Step 4: Display components
print("\nMatrix U:")
print(U)

print("\nSingular values (S):")
print(S)

print("\nMatrix VT:")
print(VT)

# Step 5: Convert S to diagonal matrix form for reconstruction
S_matrix = np.zeros((n, n))
np.fill_diagonal(S_matrix, S)

# Step 6: Reconstruct the matrix
A_reconstructed = U @ S_matrix @ VT

print("\nReconstructed Matrix:")
print(A_reconstructed)

