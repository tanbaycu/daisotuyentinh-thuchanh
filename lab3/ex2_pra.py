import numpy as np
n = int(input("Nhap n: "))
a = np.array([50 - 5*k for k in range(n)])
b = np.array([-10 + 3*k for k in range(n)])
c = np.array([(-1)**k/(2*k+1) for k in range(n)])
d = np.array([(1)/(k**2) for k in range(1, n)])
e = np.array([k/(k**2+1) for k in range(1, n)])
# Fibonancii
fib = [1, 1]
while len(fib) < n:
    fib.append(fib[-1] + fib[-2])
f = np.array([1/fib[k] for k in range(n)])
# Lucas
lucas = [2, 1]
while len(lucas) < n:
    lucas.append(lucas[-1] + lucas[-2])
g = np.array([1/lucas[k] for k in range(n)])


print(a, b, c, d, e, g, f)
