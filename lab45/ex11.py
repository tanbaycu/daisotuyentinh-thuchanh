import numpy as np


A = np.array([[2, 4, 1],
              [6, 7, 2],
              [3, 5, 9]])


is_square = (A.shape[0] == A.shape[1])
print(f"Ma trận A vuông {is_square}")
symmetry = np.array_equal(A, A.T)
print(f"Ma trận A đối xứng {symmetry}")
skew = np.array_equal(A, -A.T)
print(f"Ma trận A bất đối xứng {skew}")
U = np.triu(A)
print(f"Ma trận tam giác trên A: \n", U)

L = np.tril(A)
print(f"Ma trận tam giác dưới A: \n", L)
