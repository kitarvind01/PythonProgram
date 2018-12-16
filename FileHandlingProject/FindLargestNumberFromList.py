array = [int(x) for x in input("Enter element of the List").split()]
array.sort()
print("Maximum value of the list is",max(array))
print("Minimum value of the list is",min(array))
print("Sorted list is",array)