from itertools import *
a = list(product("ЕКМОПРТЬ", repeat=5))
q1 = q2 = 0
for x in a:
    q1 += 1
    if x.count("К") == 0 and x.count("Р") == 2:
        print(q1)

d = {0: "Е", 1: "К", 2: "М", 3: "О", 4: "П", 5: "Р", 6: "Т", 7: "Ь"}
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
                    q2 += 1
                    if p.count("К") == 0 and p.count("Р") == 2:
                        print(q2)