import numpy as np

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def invest_3d_sý(A, d, title="Linear System 3D:
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    A_bar = np.hstack((A, d
    


    rank_A = np.linalg.matrix_rank(A)
    rank_Abar = np.linalg.matrix_rank(A_bar)
    
    n = 3

    print(f"Hệ Phương Trình: {title}")
    print(f"Rank(A) = {rank_A}; Rank(A_bar) = {rank_Abar}")
    

    sol = None

    if rank_A<rank_Abar:
        print("Vô Nghiệm")
    elif rank_A==rank_Abar==n:
        print("Duy Nhất")
        sol = np.linalg.solve(A, b)
    else:
        print("Vô Số Nghiệm")


    fig = plt.figure(figsize=(9, 7))
    ax = fig.add_subplot(111, projection="3d")

    x_range = np.linspace(-5, 5, 20)
    y_range = np.linspace(-5, 5, 20)
    X, Y = np.meshgrid(x_range, y_range)


    colors = ['autumn', 'summer', 'winter']
    plane_labels = ['eq1', 'eq2', 'eq3']

    for i in range(3):
        a_i, b_i, c_i = A[i, 0], A[i, 1], A[i, 2]
        d_i = d[i, 0]

        if abs(c_i) > 1e-6:
            Z = (d_i - a_i*X - b_i*Y) / c_i
            surf = ax.plot_surface(X, Y, Z, alpha=0.5, cmap=colors[i])
        else:
            if abs(b_i) > 1e-6:
                Y_plane = (d_i - a_i * X) / b_i
                Z_range = np.linspace(-5,5, 20)
                X_m, Z_m = np.meshgrid(x_range, Z_range)
                ax.plot_surface(X_m, Y_m, Z_m, alpha=0.5, cmap=colors[i])
            
    if sol is not None:
        ax.scatter([sol[0]], [sol[1]], [sol[2]], color="red", marker="o", s=80, marker='o', label='Nghiệm')
        ax.legend()

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    plt.title(title)
    
                

            

        
        

    
    
        