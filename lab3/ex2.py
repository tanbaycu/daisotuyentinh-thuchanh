import numpy as np
import math


n = int(input("Nhap n: "))

a = np.array([12 + 2 * k for k in range(n)])
b = np.array([31 + 2 * k for k in range(n)])
c = np.array([k+5 for k in range(n)])
d = np.array([-5+k for k in range(n)])
e = np.array([10 + (-2) * k for k in range(n)])

w = np.array([1/(2**k) for k in range(n)])
j = np.array([1/(k**2+1) for k in range(n)])
p = np.array([0 + (k/(k+1)) for k in range(n)])

fib = [1, 1]
while len(fib) < n:
    fib.append(fib[-1] + fib[-2])
g = np.array([1/fib[k] for k in range(n)])

def songuyento(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n%i==0:
            return False
    return True

count = 0
num_try = 2
res = []

while count < n:
    if songuyento(num_try) == True:
        res.append(1/num_try)
        count += 1
    num_try  += 1


l = np.array([k * (k+1) / 2 for k in range(1, n+1)])
i = np.array([chr(k) for k in range(ord('a'), ord('z') + 1)])
m = np.array([chr(ord('A') + k*3) for k in range(n)])




print(a, b, c, d, e, w, j, p, g, res, l, i, m,  sep="\n")