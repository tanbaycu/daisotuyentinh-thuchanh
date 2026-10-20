import numpy as np
n = int(input("Nhap n: "))

x = np.logspace(0, -(n-1), n, base=10)
print(x)
