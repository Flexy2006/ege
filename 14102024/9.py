from itertools import *
a = list(product("МАТВЕЙ", repeat=6))
q1 = q2 = 0
for x in a:
    flag = 0
    if len(x) == len(set(x)):
        for i in range(len(x) - 1):
            if x[0] == "Й" or (x[i] == "А" and x[i + 1] == "Е"):
                flag = 1
        if flag == 0:
            q1 += 1
print(q1)


d = {0: "М", 1: "А", 2: "Т", 3: "В", 4: "Е", 5: "Й"}
for a1 in range(len(d)):
    for a2 in range(len(d)):
        for a3 in range(len(d)):
            for a4 in range(len(d)):
                for a5 in range(len(d)):
                    for a6 in range(len(d)):
                        p = []
                        p.append(d[a1])
                        p.append(d[a2])
                        p.append(d[a3])
                        p.append(d[a4])
                        p.append(d[a5])
                        p.append(d[a6])
                        flag = 0
                        if len(p) == len(set(p)):
                            for m in range(len(p) - 1):
                                if p[0] == "Й" or (p[m] == "А" and p[m + 1] == "Е"):
                                    flag = 1
                            if flag == 0:
                                q2 += 1
print(q2)