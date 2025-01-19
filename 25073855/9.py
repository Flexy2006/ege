from itertools import *
a = open('1000.txt')
q = 1
n = 0
for i in a:
    b = [int(j) for j in i.split()]
    if len(set(b)) == 3:
        print(int(list(set(b))[2]), set(b), b, q)
    q += 1
print(n)