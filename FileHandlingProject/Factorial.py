def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f



x= int(input("Enter any value to find the factorial"))
result= fact(x)
print("The factorial of",x,"is",result)