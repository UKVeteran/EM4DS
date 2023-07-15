
# importing Numpy package
import numpy as np
  
# creating a 3X3 Numpy matrix
n_array = np.array([[1,1,6],
                    [2,3,5],
                    [6,-2,-7]])
  
# Displaying the Matrix
print("Numpy Matrix is:")
print(n_array)
  
# calculating the determinant of matrix
det = np.linalg.det(n_array)
  
print("\nDeterminant of given 3X3 square matrix:")
print(int(det))