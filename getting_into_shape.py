import sys
import numpy as np

if len(sys.argv) < 2:
    print("no option chosen")

elif sys.argv[1] == "1":
    temperatures = np.array([
        29.3, 42.1, 18.8, 16.1, 38.0, 12.5,
        12.6, 49.9, 38.6, 31.3, 9.2, 22.2
    ]).reshape(2, 2, 3)

    print(temperatures.shape)
    print(temperatures)

    print(np.swapaxes(temperatures, 1, 2))

elif sys.argv[1] == "2":
    table = np.array([
        [5, 3, 7, 1],
        [2, 6, 7 ,9],
        [1, 1, 1, 1],
        [4, 3, 2, 0],
    ])

    print(table.max())
    print(table.max(axis=0))
    print(table.max(axis=1))

elif sys.argv[1] == "3":
    A = np.arange(32).reshape(4, 1, 8)
    print(A)

    B = np.arange(48).reshape(1, 6, 8)
    print(B)

    print(A + B)