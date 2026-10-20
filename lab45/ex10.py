import numpy as np


A = np.array([[-1, 4, 8],
              [-9, 1, 2]])
B = np.array([[5, 8],
              [0, -6],
              [5, 6]])
C = np.array([[-4, 1],
             [6, 5]])
D = np.array([[-6, 3, 1],
              [8, 9, -2],
              [6, -1, 5]])


# Cộng trừ ma trận -> phải cùng kích thước
# Nhân ma trận thì số cột phải bằng số hàng


print('a', None)
print('b', np.dot(B, C.T))
print('c', C - C.T)
print('d', D - D.T)
print('e', D.T.T)
print('f', 2*C.T)
print('g', A.T + B)
print('h', (A.T + B).T)
print('i', (2*A.T - 5*B).T)
print('j', -(D).T)
print('k', -(D.T))
print('l', np.linalg.matrix_power(C, 2).T)
print('m', np.linalg.matrix_power(C.T, 2))