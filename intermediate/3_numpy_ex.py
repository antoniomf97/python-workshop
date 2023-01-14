"""
Python Libraries - Numpy

NumPy is a library for efficient array computations, modeled after Matlab. 
Arrays differ from plain Python lists in the way they are stored and handled. 
Array elements stay together in memory, so they can be quickly accessed. 
NumPy also supports quick subindexing.

NumPy provides vectorized mathematical functions. When, e.g., you call numpy.sin(a), 
the sine function is applied on every element of array a. This is done using compiled C code, 
so it works much faster than a Python for loop, even faster than list comprehensions

https://numpy.org/
"""

# import numpy as np
# from numpy.linalg import inv


# print("pi =", np.pi)
# print("e =", np.e)
# print()

# arr1 = [1, 2, 3]
# arr2 = np.array([1, 2, 3])
# print(arr1 * 3)
# print(arr2 * 3)
# print()

# arr3 = np.array([4, 5, 6])

# print(arr2 + arr3)
# print(arr2 * arr3)
# print()

# m1 = np.matrix([[1, 2], [3, 4]])
# m2 = np.matrix([[5, 7], [8, 11]])
# print(m1 * m2)
# print(m1.transpose())
# print(inv(m1))
# print()

# print("sin(pi/2) =", np.sin(np.pi/2))
# print("cos(pi/2) =", np.cos(np.pi/2))

# print("tan(pi/2)", np.tan(np.pi/2))
# print("tan(-pi/2)", np.tan(-np.pi/2))
# print()

# print("exp(10) =", np.exp(10))
# print()

# print(np.arange(10000).reshape(100, 100))
