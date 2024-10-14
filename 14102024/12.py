from itertools import *
a = list(product("01234567", repeat=5)) 
q1 = q2 = 0
for x in a:
    if x.count("6") == 1 and x[0] != "0":
        flag = 0
        for i in range(len(x) - 1):
            if (int(x[i]) % 2 == 1 and x[i + 1] == "6") or (int(x[i + 1]) % 2 == 1 and x[i] == "6"):
                flag = 1
        if flag == 0:
            q1 += 1
print(q1)


d = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7"}
for a1 in range(len(d)):
    for a2 in range(len(d)):
        for a3 in range(len(d)):
            for a4 in range(len(d)):
                for a5 in range(len(d)):
                    p = []
                    p.append(d[a1])
                    p.append(d[a2])
                    p.append(d[a3])
                    p.append(d[a4])
                    p.append(d[a5])
                    if p.count("6") == 1 and p[0] != "0":
                        fl = 0
                        for m in range(len(p) - 1):
                            if (int(p[m]) % 2 == 1 and p[m + 1] == "6") or (int(p[m + 1]) % 2 == 1 and p[m] == "6"):
                                fl = 1
                        if fl == 0:
                            q2 += 1
print(q2)