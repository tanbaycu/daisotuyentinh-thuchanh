import numpy as np

A = np.array([[2, 4, 1], [6, 7, 2], [3, 5, 9]])

x1 = A[0, :]
Y = A[1:, :]

print(x1, Y)