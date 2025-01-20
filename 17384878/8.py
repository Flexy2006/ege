from itertools import *
a = 0
for x in product('0123456', repeat=4):
    if x[0] != '0' and x[0] > x[1] > x[2] > x[3]:
        a += 1
print(a)