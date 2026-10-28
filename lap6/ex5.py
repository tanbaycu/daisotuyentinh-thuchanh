import numpy as np
from scipy.linalg import lu


A = np.array([[1, 2, 1],
              [2, 2, 2],
              [2, 4, 1]])

b = np.array([1, 1, 2])

A_inv = np.linalg.inv(A)
x_me1 = A_inv @ b

print(f"x = {x_me1[0]:4f}, y = {x_me1[1]:4f}, z = {x_me1[2]:4f}")

def khu_gauss(A_in, b_in):
    M = np.hstack([A_in.astype(float), b_in.reshape(-1, 1).astype(float)])
    n = len(b_in)

    for k in range(n - 1):
        for i in range(k+1, n):
            factor = M[i, k] / M[k, k]
            M[i, k:] -= factor * M[k, k:]
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (M[i, -1] - np.dot(M[i, i+1:n], x[i+1:n])) / M[i, i]
    # Triệt tiêu -0.0 và sai số dấu phẩy động cực nhỏ
    # x = np.where(np.abs(x) < 1e-12, 0.0, x)
    return x

x_me2 = khu_gauss(A, b)
print(f"x = {x_me2[0]:4f}, y = {x_me2[1]:4f}, z = {x_me2[2]:4f}")

def phan_tich_lu(A_in, b_in):
    P, L, U = lu(A_in)
    Pb = P.T @ b_in
    n = len(b_in)
    y = np.zeros(n)
    for i in range(n):
        y[i] = (Pb[i] - np.dot(L[i, :i], y[:i]))

    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (y[i] - np.dot(U[i, i+1:], x[i+1:])) / U[i, i]
    # Triệt tiêu -0.0 và sai số dấu phẩy động cực nhỏ
    x = np.where(np.abs(x) < 1e-12, 0.0, x)
    return x

x_me3 = phan_tich_lu(A, b)
print(f"x = {x_me3[0]:4f}, y = {x_me3[1]:4f}, z = {x_me3[2]:4f}")