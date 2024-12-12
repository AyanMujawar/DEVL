import numpy as np

def create_matrix(rows, cols):
    matrix = []
    print("Enter the elements:")
    for i in range(rows):
        a = []
        for j in range(cols):
            while True:
                try:
                    # Input for each element
                    element = int(input(f"Element [{i+1}, {j+1}]: "))
                    a.append(element)
                    break
                except ValueError:
                    print("Invalid input! Please enter an integer.")
        matrix.append(a)
    return np.array(matrix)

# Get dimensions for the first matrix
matrix1_rows = int(input("Enter the number of rows for Matrix 1: "))
matrix1_cols = int(input("Enter the number of columns for Matrix 1: "))
matrix1 = create_matrix(matrix1_rows, matrix1_cols)

# Get dimensions for the second matrix
matrix2_rows = int(input("Enter the number of rows for Matrix 2: "))
matrix2_cols = int(input("Enter the number of columns for Matrix 2: "))
matrix2 = create_matrix(matrix2_rows, matrix2_cols)

# Addition and Subtraction
if matrix1.shape == matrix2.shape:
    add_matrix = np.add(matrix1, matrix2)
    print("Addition matrix:")
    print(add_matrix)
    
    sub_matrix = np.subtract(matrix1, matrix2)
    print("Subtraction matrix:")
    print(sub_matrix)
else:
    print("Error: Matrices must have the same shape for addition and subtraction.")

# Multiplication
if matrix1_cols == matrix2_rows:
    multi_matrix = np.matmul(matrix1, matrix2)
    print("Multiplication matrix:")
    print(multi_matrix)
else:
    print("Error: Number of columns in Matrix 1 must be equal to the number of rows in Matrix 2 for multiplication.")
