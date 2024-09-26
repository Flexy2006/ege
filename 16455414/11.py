a = open("1000.txt")
q = 0
for i in a:
    b = [int(j) for j in i.split()]
    d = []
    for x in b:
        if b.count(x) == 2:
            d.append(x)
        if b.count(x) > 2:
            break
    if len(d) == 4 and len(set(d)) == 2:
        if sum(d)/4 < (sum(b) - sum(d))/3:
            q += 1
print(q)#96