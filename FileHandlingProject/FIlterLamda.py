from functools import reduce

nums=[2,3,4,5,6,7,8,1,2,3,4,5]

evenNums= list(filter(lambda n:n%2==0,nums))
print(evenNums)

double= list(map(lambda n:n*2,evenNums))
print(double)

sum= reduce(lambda a,b:a+b,double)
print(sum)