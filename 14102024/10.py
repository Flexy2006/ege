from itertools import *
a = list(product("ГЕРАСИМ", repeat=7))
sogl = "ГРСМ"
gl = "ЕАИ"
q1 = q2 = 0
for x in a:
    flag = 0
    if len(x) == len(set(x)):
        for i in range(len(x) - 1):
            if (x[i] in sogl and x[i + 1] in sogl) or (x[i] in gl and x[i + 1] in gl):
                flag = 1
        if flag == 0:
            q1 += 1
print(q1)


d = {0: "Г", 1: "Е", 2: "Р", 3: "А", 4: "С", 5: "И", 6: "М"}
for a1 in range(len(d)):
    for a2 in range(len(d)):
        for a3 in range(len(d)):
            for a4 in range(len(d)):
                for a5 in range(len(d)):
                    for a6 in range(len(d)):
                        for a7 in range(len(d)):   
                            p = []
                            p.append(d[a1])
                            p.append(d[a2])
                            p.append(d[a3])
                            p.append(d[a4])
                            p.append(d[a5])
                            p.append(d[a6])
                            p.append(d[a7])
                            fl = 0
                            if len(p) == len(set(p)):
                                for m in range(len(p) - 1):
                                    if (p[m] in sogl and p[m + 1] in sogl) or (p[m] in gl and p[m + 1] in gl):
                                        fl = 1
                                if fl == 0:
                                    q2 += 1
print(q2)