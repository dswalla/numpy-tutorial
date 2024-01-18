import numpy as np
from numpy.random import default_rng

print("----------")
print("Masks")

numbers = np.linspace(5, 50, 24, dtype=int).reshape(4, -1)
print("----------")
print(numbers)

mask = numbers % 4 == 0
print("----------")
print(mask)

print("----------")
print(numbers[mask])

by_four = numbers[numbers % 4 == 0]
print("----------")
print(by_four)

print("----------")
print("Filtering")

rng = default_rng()
values = rng.standard_normal(10000)
print("----------")
print(values[:5])

std = values.std()
print("----------")
print(std)

filtered = values[(values > -2 * std) & (values < 2 * std)]
print("----------")
print(filtered.size)

print("----------")
print(values.size)

print("----------")
print(filtered.size / values.size)