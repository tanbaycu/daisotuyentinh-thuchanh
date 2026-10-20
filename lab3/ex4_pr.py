import numpy as np


r1 = np.array([1, 0, 2])
r2 = np.array([0, 3, 0])
r3 = np.array([4, 0, 5])

x = np.vstack((r1, r2, r3))
y = np.diag(x)

print(x, y)