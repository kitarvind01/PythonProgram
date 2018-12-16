def add(x,y):
    return x+y

def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choose= input("Enter choice(1/2/3/4):")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choose=='1':
    print(num1,"+",num2,"=",add(num1,num2))

elif choose=='2':
    print(num1,"-",num2,"=",sub(num1,num2))

elif choose=='3':
    print(num1,"*","=",mul(num1,num2))

elif choose=='4':
    print(num1,"/",num2,"=",div(num1,num2))
else:
    print("Entered number is not valid")




