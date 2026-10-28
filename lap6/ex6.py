import numpy as np
import matplotlib.pyplot as plt


t_p = np.array([1, 2, 3], dtype=float)
v_p = np.array([6, 15, 38], dtype=float)

A = np.column_stack([t_p**0, t_p**1, t_p**2])
print(A)

a = np.linalg.solve(A, v_p)
a0, a1, a2 = a[0], a[1], a[2]

print(f"a0 = {a0}")
print(f"a1 = {a1}")
print(f"a2 = {a2}")
print(f"-> Đa thức nội suy: p(t) = {a0:.0f} + {a1:.0f}t + {a2:.0f}t^2")


t_de = np.linspace(0.5, 3.5, 200)
p_de = a0 + a1 * t_de + a2 * (t_de ** 2)

plt.figure(figsize=(7, 5))
plt.plot(t_de, p_de, 'b-', label=r'$p(t) = 11 -12t + 7t^2$', linewidth=2)
plt.plot(t_p, v_p, 'ro', markersize=8, label='Data points')

for x_val, y_val in zip(t_p, v_p):
    plt.text(x_val + 0.05, y_val - 1.5, f"({int(x_val)}, {int(y_val)})", fontsize=11, color='darkred')


plt.xlabel('t')
plt.ylabel('p(t)')
plt.title('Ex6')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend
plt.show()