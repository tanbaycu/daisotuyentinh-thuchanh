import numpy as np

P = np.array([2, 1, 3])
S = np.array([[12, 15, 10, 16, 12], 
             [5, 9, 14, 7, 10],
             [8, 12, 10, 9, 15]])


days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
total_sales = np.dot(P, S)

for day, total in zip(days, total_sales):
    print(f"{day}: ${total}")
print(total_sales)


