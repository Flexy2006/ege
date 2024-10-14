from itertools import *
a = list(product("КЛРТ", repeat=4))
q1 = q2 = 0
for x in a:
    q1 += 1
    if q1 == 67:
        print(x)

d = {0: "К", 1: "Л", 2: "Р", 3: "Т"}
for a1 in range(len(d)):
    for a2 in range(len(d)):
        for a3 in range(len(d)):
            for a4 in range(len(d)):
                q2 += 1
                if q2 == 67:
                    print(d[a1], d[a2], d[a3], d[a4])
                    break