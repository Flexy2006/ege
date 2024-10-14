from itertools import *
a = list(product(sorted("АЛГОРИТМ"), repeat=4))
q1 = q2 = 0
for x in a:
    q1 += 1
    if x[0] == "И" and x[1] == "Г":
        print(q1)

d = {0: "А", 1: "Г", 2: "И", 3: "Л", 4: "М", 5: "О", 6: "Р", 7: "Т"}
for a1 in range(len(d)):
    for a2 in range(len(d)):
        for a3 in range(len(d)):
            for a4 in range(len(d)):
                q2 += 1
                if d[a1] == "И" and d[a2] == "Г":
                    print(q2)