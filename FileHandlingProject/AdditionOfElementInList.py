listArray= [int(x) for x in input("Enter the element of list").split()]
add=0
lengthOfListArray= len(listArray)
for i in range(lengthOfListArray):
    add= add+listArray[i]
print("Addition of the element of the List is=",add)