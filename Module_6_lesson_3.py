import numpy
# print("numpy imported successfully!") 

import numpy as npy
# print("successful")

#Generating an array of numbers between 1 and 100 with both numbers included 
list = npy.arange(1, 101)
print(list)

#Generating all the even integers from 1 to 100 in the list
array1 = npy.arange(2,101,2)
print(array1)

x = npy.lcm.reduce(array1)
print('\nThe LCM of the Even numbers in the array is: ', x)



