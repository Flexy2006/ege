from itertools import *
a = list(product("012345678", repeat=5))
q1 = q2 = 0
for x in a:
    if x[0] > x[1] > x[2] > x[3] > x[4] and x[0] != 0:
        q1 += 1
print(q1)

d = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8"}
for a1 in range(len(d)):
    for a2 in range(len(d)):
        for a3 in range(len(d)):
            for a4 in range(len(d)):
                for a5 in range(len(d)):
                    if int(a1) > int(a2) > int(a3) > int(a4) > int(a5) and int(a1) != 0:  
                        q2 += 1
print(q2)