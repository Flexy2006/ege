a = open('1000.txt')
q = 0
for i in a:
    b = [int(j) for j in i.split()]
    pov = []
    nepov = []
    for j in range(len(b)):
        if b.count(b[j]) == 3:
            pov.append(b[j])
        if b.count(b[j]) == 1:
            nepov.append(b[j])
    if len(pov) == 3 and len(nepov) == 3:
        if ((sum(pov)) ** 2) > ((sum(nepov)) ** 2):
            q += 1
print(q)