import numpy as np

A = np.array([[3.0, 3.2],
              [3.5, 3.6]], float)
b = np.array([118.4, 135.2], float)

sol = np.linalg.solve(A, b)
n1, n2 = sol[0], sol[1]
print(n1, n2)
