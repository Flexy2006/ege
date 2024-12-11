from itertools import *
a = open('1000.txt')
q = 0
for i in a:
    b = [int(j) for j in i.split()]
    if max(b) < sum(b) - max(b):
        if b[0]+b[1] == b[2] + b[3] or b[0]+b[2] == b[1] + b[3] or b[0]+b[3] == b[2] + b[1]:
            q += 1



print(q)