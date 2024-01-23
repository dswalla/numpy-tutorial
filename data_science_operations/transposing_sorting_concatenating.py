import numpy as np

print("Transposing")
print("-----------------")

a = np.array([
    [1,2],
    [3,4],
    [5,6]
])

print(a.T)
print("-----------------")

print(a.transpose())
print("-----------------")

print("Sorting")
print("-----------------")

data = np.array([
    [7,1,4],
    [8,6,5],
    [1,2,3]
])

print(np.sort(data))
print("-----------------")

print(np.sort(data, axis=None))
print("-----------------")

print(np.sort(data, axis=0))
print("-----------------")