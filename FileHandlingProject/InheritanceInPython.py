class A:
    def __init__(self):
        print("In A init method")
    def feature1(self):
        print("Inside feature 1")
    def feature2(self):
        print("inside feature 2")

class B:
    def __init__(self):
        super().__init__()
        print("In B init")
    def feature3(self):
        print("Inside feature3")

class C(A,B):
    def __init__(self):
        print("in C init method")
    def feature4(self):
        print("Inside feature 4")

a1= C()
a1.feature3()

