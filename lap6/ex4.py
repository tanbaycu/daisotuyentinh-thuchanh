import numpy as np
from scipy.linalg import lu


A = np.array([[1, 1, 2],
              [3, 6, -5],
              [2, 4, -3]], dtype = float)
b = np.array([1, -1, 0], dtype = float)

detA = np.linalg.det(A)
is_invertible = not np.isclose(detA, 0)
print(f"(a) det(A)= {detA:.4f}, làm tròn: {np.round(detA)}")
print(f"Ma trận A có khả nghịch không?", 'Có' if is_invertible else 'Không')

A_inv = np.linalg.inv(A)
x_inv = A_inv @ b
print(f"(b) Nghiệm dùng ma trận nghịch đảo: ")
print(f"x = {x_inv[0]:.4f}, y = {x_inv[1]:.4f}, z = {x_inv[2]:.4f}")


def khu_gauss(A_mat, b_vec):
    n = len(b_vec)
    M = np.hstack([A_mat.astype(float), b_vec.reshape(-1, 1).astype(float)])

    for k in range(n - 1):
        for i in range(k+1, n):
            factor = M[i, k] / M[k, k]
            M[i, k:] -= factor * M[k, k:]
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (M[i, -1] - np.dot(M[i, i+1:n], x[i + 1:n])) / M[i, i]
    return x

x_gauss = khu_gauss(A, b)
print(f"(c) Nghiệm dùng phương pháp Gauss:")
print(f"x = {x_gauss[0]:.4f}, y = {x_gauss[1]:.4f}, z = {x_gauss[2]:.4f}")


def khu_gauss_phantutruc(A_mat, b_vec):
    n = len(b_vec)
    M = np.hstack([A_mat.astype(float), b_vec.reshape(-1, 1).astype(float)])
    for k in range(n - 1):
        pivot_row = k + np.argmax(np.abs(M[k:, k]))
        if pivot_row != k:
            M[[k, pivot_row]] = M[[pivot_row, k]]

        for i in range(k+1, n):
            factor = M[i, k] / M[k, k]
            M[i, k:] -= factor * M[k, k:]
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (M[i, -1] - np.dot(M[i, i+1:n], x[i + 1:n])) / M[i, i]
    return x

x_pivot = khu_gauss_phantutruc(A, b)
print(f"(d) Nghiệm dùng phương pháp Gauss với chọn phần tử trụcc")
print(f"x = {x_pivot[0]:.4f}, y = {x_pivot[1]:.4f}, z = {x_pivot[2]:.4f}")



P, L, U = lu(A)

Pb = P.T @ b
n = len(b)

y = np.zeros(n)
for i in range(n):
    y[i] = (Pb[i] - np.dot(L[i, :i], y[:i])) 

x_lu = np.zeros(n)
for i in range(n-1, -1, -1):
    x_lu[i] = (y[i] - np.dot(U[i, i+1:], x_lu[i+1:])) / U[i, i]

print(f"(e) Nghiệm dùng phương pháp LU:")
print(f"x = {x_lu[0]:.4f}, y = {x_lu[1]:.4f}, z = {x_lu[2]:.4f}")

        
        
