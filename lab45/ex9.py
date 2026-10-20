import numpy as np



T = np.array([[0.6, 0.7],
              [0.4, 0.3]])
p = np.array([[0.5],
              [0.5]])

k_list = [1, 2, 10, 100, 10000]

for k in k_list:
    tk = np.linalg.matrix_power(T, k) # lũy thừa ma trận
    pk = np.dot(tk, p)
    print(f"k = {k}:")
    print(pk)