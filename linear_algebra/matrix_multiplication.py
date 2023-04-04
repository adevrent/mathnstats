import numpy as np

# Define 3x3 Matrix A.
A = np.array([[1, 2, 3],
     [2, 5, 2],
     [6,-3, 1]])

# Define 3x1 vector x.
x = np.array([0, 0, 2])

# Calculate A * x.
print(A@x)