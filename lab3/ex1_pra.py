import numpy as np


u = np.array([4.5, -2.1, 0.0, 7.8, -11.2, 3.4])
v = np.array([100, 200, 300])

print(u.size, len(v))
if len(u) > len(v):
    print("A dai hon B")
    print("Do chenh lech la: ", len(u) - len(v))
