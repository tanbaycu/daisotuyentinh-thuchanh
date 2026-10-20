import numpy as np

n = 5
A = np.random.randint(1, 10, size=(n, n))
B = np.random.randint(1, 10, size=(n, n))

# Tính det(A+B) - det(A) - det(B)
result_5x5 = np.linalg.det(A + B) - np.linalg.det(A) - np.linalg.det(B)

print(f"1. Với ma trận 5x5:")
print(f"   det(A+B) - det(A) - det(B) = {result_5x5:.2f}")

print("\n2. Lặp lại với 3 kích thước n x n khác nhau:")
other_n_values = [2, 3, 4]

for n in other_n_values:
    A_n = np.random.randint(1, 10, size=(n, n))
    B_n = np.random.randint(1, 10, size=(n, n))
    
    diff = np.linalg.det(A_n + B_n) - np.linalg.det(A_n) - np.linalg.det(B_n)
    print(f"   - Kích thước {n}x{n}: det(A+B) - det(A) - det(B) = {diff:.2f}")

print("\n=> Kết luận: False! Vì kết quả khác 0 nên det(A + B) KHÔNG BẰNG det(A) + det(B).")