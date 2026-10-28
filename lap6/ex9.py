import numpy as np
M = np.array([[0.61, 0.29, 0.15],
              [0.35, 0.59, 0.063],
              [0.04, 0.12, 0.787]], float)

detM = np.linalg.det(M)
print(f"det(M) = {detM:.6f}")

M_inv = np.linalg.inv(M)
print(f"M_inv = {np.round(M_inv, 4)}")

print(f"R = {M_inv[0,0]:.4f}*X + ({M_inv[0,1]:.4f})*Y + ({M_inv[0,2]:.4f})*Z")
print(f"G = {M_inv[1,0]:.4f}*X + ({M_inv[1,1]:.4f})*Y + ({M_inv[1,2]:.4f})*Z")
print(f"B = {M_inv[2,0]:.4f}*X + ({M_inv[2,1]:.4f})*Y + ({M_inv[2,2]:.4f})*Z")