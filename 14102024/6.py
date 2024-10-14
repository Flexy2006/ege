from itertools import *
a = list(product(sorted("МАНГУСТ"), repeat=6))
q1 = q2 = 0
for x in a:
    q1 += 1
    if x[0] != "У" and x.count("М") == 2 and x.count("Г") <= 1:
        print(q1)


d = {0: "А", 1: "Г", 2: "М", 3: "Н", 4: "С", 5: "Т", 6: "У"}
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
                        q2 += 1
                        if d[a1] != "У" and p.count("М") == 2 and p.count("Г") <= 1:
                            print(q2)