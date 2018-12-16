import sys
def sum(a,*b):
    c=a
    for i in b:
        c=c+b[i]
    print(c)

a=int(input("Enter the first number"))
b= input("ENter the second number")
sum(a,tuple(list(b)))