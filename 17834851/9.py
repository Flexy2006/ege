a = open('1000.txt')
q = 0
for i in a:
    pov = []
    nepov = []
    b = [int(j) for j in i.split()]
    for l in b:
        if b.count(l) == 2:
            pov.append(l)
        if b.count(l) == 1:
            nepov.append(l)
    if len(pov) == 2 and len(nepov) == 4:
        if sum(nepov)/len(nepov) <= sum(pov):
            q += 1
print(q)