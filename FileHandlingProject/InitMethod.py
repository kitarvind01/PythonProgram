class InitMethod:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram

    def m1(self):
        print("config of computer is",self.cpu,self.ram)

tes1 = InitMethod('i3',8)
tes2= InitMethod('i5',16)
tes1.m1()
tes2.m1()