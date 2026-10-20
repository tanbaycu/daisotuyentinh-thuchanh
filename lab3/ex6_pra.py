import numpy as np

v = np.array([15, -4, 28, 9, -17, 33, 42, -8, 55, 60, 102, -3])


a = v[:4]
b = v[-6:]
c = v[[1,  4, -1]]
d = v[3:9]
e = v[::2]


print(a, b, c, d, e)