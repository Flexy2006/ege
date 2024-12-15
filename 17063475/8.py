from itertools import *
q = 0
a = "357"
b = "2460"
c = "246"
for x in (product(a,b,a,b,a)):
    if len(x) == len(set(x)):
        q += 1
for x in (product(c,a,b,a,b)):
    if len(x) == len(set(x)):
        q += 1
print(q)