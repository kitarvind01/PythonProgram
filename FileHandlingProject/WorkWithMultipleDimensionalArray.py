from numpy import *
#array()
#linspace()
#logspace()
#arange()
#zeros()
#ones()

#array
arr1= array([2,1,23,45,6677])
arr2=array([3,4,45,677,88,])
arr3=arr1+arr2
print(arr3)
#linspace
arr2= linspace(0,10)

print(arr2)

#arange

arr3= arange(1,50,3)
print(arr3)


#zeros
arr4=zeros(5,int)
print(arr4)

#ones
arr5= ones(10,int)
print(arr5)


# Adding of two array or adding a particular value to array element

arr6= array([2,3,1,2,3,4,5,6])
arr6=arr6+5
print(arr6)

arr7=([14,3,2,4,5,6])
arr8=([2,3,4,5,6,7])
arr7=arr7 + arr8
print(arr7)