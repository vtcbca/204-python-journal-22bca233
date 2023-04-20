#script to create a 3X3 matrix with values ranging from 2 to 10.output contain dimention , size and array bytes in memory.

import numpy as np

a1 = np.arange(2,11).reshape(3,3)
print(f"Your 3x3 matrix:\n{a1}")
print(f"Dimention of array is = {a1.ndim}\nsize of array = {a1.size}\nBytes occupied in memory = {a1.size*a1.itemsize}")
