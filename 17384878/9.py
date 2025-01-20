a = open('1000.txt')
count = 0
for i in a:
    b = [int(j) for j in i.split()]
    povtor = []
    nepovtor = []
    for i in range(len(b)):
        if b.count(b[i]) == 2:
            povtor.append(b[i])
        if b.count(b[i]) == 1:
            nepovtor.append(b[i])
    if len(povtor) == 4 and len(nepovtor) == 3 and sum(povtor)/4 > sum(nepovtor)/3:
        count += 1
print(count) 