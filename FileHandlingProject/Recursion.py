import sys

print(sys.getrecursionlimit())
sys.setrecursionlimit(2000)
i=0
def fact():
    global i
    i+=1
    print("Hello",i)
    fact()

fact()