import random
import time
t1=time.time()
mylist = random.sample(range(1, 1000001), 10000)
myset = set(mylist)
for i in range(10000):
    x = random.randint(1, 1000000)
    x in myset
print("set took ",time.time()-t1," seconds")
t2=time.time()
for i in range(10000):
    x = random.randint(1, 1000000)
    x in mylist
print("list took ",time.time()-t2," seconds")