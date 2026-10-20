import numpy as np

n = int(input("nhap n:  "))

x = np.logspace(1, n, num = n, dtype=int)

print(x)