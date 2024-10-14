from itertools import *
a = list(product("ABCDXYZ", repeat=4))
q1 = q2 = 0
s = "XYZ"
for x in a:
    if x[0] in s and x[1] not in s and x[2] not in s and x[3] not in s:
        q1 += 1
print(q1)

d = {0: "A", 1: "B", 2: "C", 3: "D", 4: "X", 5: "Y", 6: "Z"}
for a1 in range(len(d)):
    for a2 in range(len(d)):
        for a3 in range(len(d)):
            for a4 in range(len(d)):
                if d[a1] in s and d[a2] not in s and d[a3] not in s and d[a4] not in s:
                    q2 += 1
print(q2)