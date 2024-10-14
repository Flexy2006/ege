from itertools import *
sogl = "РСМХ"
gl = "ОА"
q1 = q2 = 0
for x in permutations("РОСОМАХА"):
    flag = 0
    for i in range(len(x) - 1):
        if (x[i] in sogl and x[i + 1] in sogl) or (x[i] in gl and x[i + 1] in gl):
            flag = 1
    if flag == 0:
        q1 += 1
print(q1 // 4)#Потому что два раза повторяется О и А, делим на 2*2!


d = {0: "Р", 1: "О", 2: "С", 3: "О", 4: "М", 5: "А", 6: "Х", 7: "А"}
for a1 in range(len(d)):
    for a2 in range(len(d)):
        for a3 in range(len(d)):
            for a4 in range(len(d)):
                for a5 in range(len(d)):
                    for a6 in range(len(d)):
                        for a7 in range(len(d)):
                            for a8 in range(len(d)):  
                                p = []
                                p.append(d[a1])
                                p.append(d[a2])
                                p.append(d[a3])
                                p.append(d[a4])
                                p.append(d[a5])
                                p.append(d[a6])
                                p.append(d[a7])
                                p.append(d[a8])
                                if p.count("Р") == 1 and p.count("С") == 1 and p.count("М") == 1 and p.count("Х") == 1 and p.count("О") == 2 and p.count("А") == 2:
                                    fl = 0
                                    for m in range(len(p) - 1):
                                        if (p[m] in sogl and p[m + 1] in sogl) or (p[m] in gl and p[m + 1] in gl):
                                            fl = 1
                                    if fl == 0:
                                        q2 += 1
print(q2//16)