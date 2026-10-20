import numpy as np

# Khởi tạo ma trận A và B theo đề bài (dùng số thực/phân số)
A = np.array([
    [2.0,   4.0,  5/2],
    [-3/4,  2.0,  1/4],
    [1/4,   1/2,  2.0]
])

B = np.array([
    [1.0,  -1/2,  3/4],
    [3/2,   1/2, -2.0],
    [1/4,   1.0,  1/2]
])

a = np.linalg.inv(A)
b = np.linalg.inv(B)




resAB = np.dot(a, b)
resAB_inv = np.linalg.inv(np.dot(A, B))
resBA_inv = np.linalg.inv(np.dot(B, A))

print('a', resAB, resAB_inv, resBA_inv)
check = np.allclose(resAB, resBA_inv)
