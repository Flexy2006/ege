from itertools import *
a = list(product("АВЕИКНОР", repeat=3))
q1 = q2 = 0
for x in a:
    print(x)
    if x.count("В") == 1:
        q1 += 1
        if x[0] != "А" and x[1] != "А" and x[2] != "А":
            print(q1)
            break

d = {0: "А", 1: "В", 2: "Е", 3: "И", 4: "К", 5: "Н", 6: "О", 7: "Р"}
for a1 in range(len(d)):
    for a2 in range(len(d)):
        for a3 in range(len(d)):
            p = []
            p.append(d[a1])
            p.append(d[a2])
            p.append(d[a3])
            if p.count("В") == 1:
                q2 += 1
                if d[a1] != "А" and d[a2] != "А" and d[a3] != "А":
                    print(q2)
                    break