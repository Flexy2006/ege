from itertools import *
a = list(product("АБЗИ", repeat=4))
q1 = q2 = 0
for x in a:
    q1 += 1
    if x[0] == "И" and x[1] == "З" and x[2] == "Б" and x[3] == "А":
        print(q1)

d = {0: "А", 1: "Б", 2: "З", 3: "И"}
for a1 in range(len(d)):
    for a2 in range(len(d)):
        for a3 in range(len(d)):
            for a4 in range(len(d)):
                q2 += 1
                if d[a1] == "И" and d[a2] == "З" and d[a3] == "Б" and d[a4] == "А":
                    print(q2)