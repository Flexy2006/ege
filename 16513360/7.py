a = open('112.txt')
q = 0
for i in a:
    q1m = []
    q1 = 0
    q2m = []
    q2 = 0
    b = [int(j) for j in i.split()]
    for k in range(len(b)):
        if b.count(b[k]) == 1:
            q1m.append(b[k])
            q1 += int(b[k])
        if b.count(b[k]) == 2:
            q2m.append(b[k])
            q2 += int(b[k])
    if len(q1m) == 4 and len(q2m) == 2:
        if q1/3<=q2:
            q+=1
print(q)
