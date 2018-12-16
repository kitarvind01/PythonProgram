def printEvenIndexValues():
    s1= input("Enter any String")
    li= list(s1.split(" "))
    stLen= len(li)
    for i in range(stLen):
         if i%2==0:
          print(li[i])

printEvenIndexValues()