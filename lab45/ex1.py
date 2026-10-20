import numpy as np

x = np.array([1, 2, 3, 4, 5])
b = np.array([1, 2, 3, 4, 5, 6])
c = np.arange(1, 31)
d = np.arange(1, 26)

print(x, b, c, d)
A = np.tile(x.reshape(-1, 1), (1, 5))
B = np.tile(b, (6, 1))
C = c.reshape(6, 5).T
D = d.reshape(5, 5).T
print(A, B, C, D)