import numpy
# print("numpy imported successfully!") 

import numpy as npy
# print("successful")

list = npy.arange(1, 101)
# print(list)


array1 = npy.arange(2,101,2)
# print("Array of all the even integers from 1 to 100")
# print(array1)

arr = npy.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100])
x = npy.lcm.reduce(arr)
print(x)


