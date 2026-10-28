import numpy as np 


A_a = np.array([[1, 2, 1],
                [2, -1, 1],
                [2, 1, 0]], dtype = float)
b_a = np.array([0, 0, 0], dtype = float)


A_b = np.array([[2, 1, 1, 1],
                [1, 2, 1, 1],
                [1, 1, 2, 1],
                [1, 1, 1, 2]], dtype = float)
b_b = np.array([1, 1, 1, 1], dtype = float)


a = np.linalg.solve(A_a, b_a)
b = np.linalg.solve(A_b, b_b)

print("a = ", np.round(a, 4))
print("b = ", np.round(b, 4))



    