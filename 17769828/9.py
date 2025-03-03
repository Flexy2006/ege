a = open('1000.txt')
count = 0
for i in a:
    povtor = []
    nepovtor = []
    secpovtor = []
    b = [int(j) for j in i.split()]
    for l in b:
        if b.count(l) >= 3:
            secpovtor.append(l)
        if b.count(l) == 1:
            nepovtor.append(l)
        if b.count(l) == 2:
            povtor.append(l)
    if len(nepovtor) >= 1 and len(secpovtor) >= 1:
        if sum(nepovtor)/len(nepovtor) < (sum(secpovtor) + sum(povtor))/(len(povtor) + len(secpovtor)):
            count += 1
print(count)