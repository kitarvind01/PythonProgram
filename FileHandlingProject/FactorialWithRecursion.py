def fact(n):
    if(n==0):
        return 1
    return n*fact(n-1)

x=int(input("Enter any number to find the factorial"))
result=fact(x)
print(result)