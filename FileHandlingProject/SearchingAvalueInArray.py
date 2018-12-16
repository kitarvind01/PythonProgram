from array import *
arr= array('i',[])

n= int(input("Enter the length of the array"))

for i in range(n):
    x=int(input("Enter the next value"))
    arr.append(x)
print(arr)

val= int(input("Enter the value to search from array"))
count=0
for e in arr:
    if e==val:
        print("The index of the element is",count)
        break
    count+=1
else:
    print("Element not found")

# Same searching the element using function to find the index of the element

print("The index of the element is",arr.index(val))



