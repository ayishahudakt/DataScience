import numpy as np

def input_matrix(name):
    print(f"Enter elements for matrix {name} (row-wise):")
    matrix = []
    for i in range(3):
        row = list(map(int, input(f"Row {i+1} (3 numbers separated by space): ").split()))
        if len(row) != 3:
            print("Please enter exactly 3 numbers.")
            return input_matrix(name)
        matrix.append(row)
    return np.array(matrix)

A = input_matrix("A")
B = input_matrix("B")
scalar = int(input("Enter a scalar value: "))

add = A + B
print("\nAddition:\n", add)

sub = A - B
print("\nSubtraction:\n", sub)

mul = np.dot(A, B)
print("\nMatrix Multiplication (A × B):\n", mul)

scalar_mul = scalar * A
print(f"\nScalar Multiplication of A by {scalar}:\n", scalar_mul)

transpose = A.T
print("\nTranspose of Matrix A:\n", transpose)

