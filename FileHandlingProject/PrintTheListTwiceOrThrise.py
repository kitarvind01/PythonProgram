list1=[2,3,4,5,6,7]
print (list1 *2)
print(list1 *3)

tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = ('physics', 'chemistry', 1997, 2000)
tup3=tup1 +tup2
print(tup3)
print(tup1*4)
print("-------------------------------------------------------------")
for i in tup1:
    print(i)

print("<----------------Print the local time-------------->")

import time
localtime= time.localtime(time.time())
print(localtime)

print("<---------Getting formated local time--------------->")

localtime1= time.asctime(time.localtime(time.time()))
print(localtime1)
