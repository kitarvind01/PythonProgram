#li=[10,12,12,1,2,11,,11,23,33]
print("Enter")
a = [int(x) for x in input().split()]
listLen= len(a)
#Even position numbers
for i in range(listLen):
    if i%2==0:
         print(a[i])
# reversing the list
#a=a[::-1]
#print(a)