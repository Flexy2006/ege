from itertools import *
a = list(product("МИТРОФАН", repeat=6))
sogl = "МТРФН"
gl = "ИОА"
q1 = q2 = 0
for x in a:
    if len(x) == len(set(x)):
        g = 0
        s = 0
        for j in x:
            if j in sogl:
                s += 1
            else:
                g += 1
        if s > g:
            flag = 0
            for i in range(len(x) - 1):
                if (x[i] in gl and x[i + 1] in gl):
                    flag = 1
            if flag == 0:
                q1 += 1
print(q1)


d = {0: "М", 1: "И", 2: "Т", 3: "Р", 4: "О", 5: "Ф", 6: "А", 7: "Н"}
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
                        fl = 0
                        if len(p) == len(set(p)):
                            g = 0
                            s = 0
                            for j in p:
                                if j in sogl:
                                    s += 1
                                else:
                                    g += 1
                            if s > g:
                                fl = 0
                                for i in range(len(p) - 1):
                                    if (p[i] in gl and p[i + 1] in gl):
                                        fl = 1
                                if fl == 0:
                                    q2 += 1
print(q2)