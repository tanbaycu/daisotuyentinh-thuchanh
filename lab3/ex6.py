import numpy as np

x = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
y = np.array([1, 3, 5, 7, 9, 11, 13, 15, 17, 19])
a = x[:6]
b= x[-5:]
c = x[[0, 4, -1]]
d = x[0:7:2]
e = y[::1]
f = x[0::2]
print(a, b, c, d, e, f)