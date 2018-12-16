from numpy import *

arr= array([
    [1,2,4,8,12,4],
    [2,3,4,5,9,8]

])
print(arr.dtype)
print(arr.ndim)
print(arr.shape)
print(arr.size)
print(arr)

arr1= arr.flatten()
print("-----------",arr1)
arr3= arr1.reshape(3,4)
print(arr3)
arr4= arr1.reshape(2,2,3)
print(arr4)