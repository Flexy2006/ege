from itertools import product
q = 0
a = "1357"
b = "2468"
for x in (product(a,b,a,b,a,b,a,b,a,b,a)):
    if x.count(x[0]) <= 4 and x.count(x[1]) <= 4 and x.count(x[2]) <= 4 and x.count(x[3]) <= 4 and x.count(x[4]) <= 4 and x.count(x[5]) <= 4 and x.count(x[6]) <= 4 and x.count(x[7]) <= 4 and x.count(x[8]) <= 4 and x.count(x[9]) <= 4 and x.count(x[10]) <= 4:
        q += 1 
for x in (product(b,a,b,a,b,a,b,a,b,a,b)):
    if x.count(x[0]) <= 4 and x.count(x[1]) <= 4 and x.count(x[2]) <= 4 and x.count(x[3]) <= 4 and x.count(x[4]) <= 4 and x.count(x[5]) <= 4 and x.count(x[6]) <= 4 and x.count(x[7]) <= 4 and x.count(x[8]) <= 4 and x.count(x[9]) <= 4 and x.count(x[10]) <= 4:
        q += 1
print(q)