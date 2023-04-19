#script to conert a list into numpy array print original list and numpyarray with its dimention,size and byte occupied in memory.
import numpy as np 

l1=[10,23.4,50,345,66]
a1=np.array(l1)
print(f"Original list:{l1}")

print(f"Numpy array:{a1}")

print(f"Dimention of array is = {a1.ndim}\nsize of array = {a1.size}\nBytes occupied in memory = {a1.size*a1.itemsize}")