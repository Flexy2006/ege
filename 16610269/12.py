a = open('1002.txt')
q = 0
for i in a:
    b = [int(j) for j in i.split()]
    rep = []
    for x in b:
        if b.count(x) == 2:
            rep.append(x)
    if len(rep) == 2 and len(set(b)) == 5:
        if sum(rep)/2 < (sum(b) - sum(rep))/4:
            q += 1
print(q)#1483