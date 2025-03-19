a = open('1000.txt')
q = 0
for i in a:
    b = [int(j) for j in i.split()]
    pov = []
    for k in b:
        if b.count(k)>1:
            pov.append(k)
    if len(pov)>0:
        if b.count(max(b)) == 1:
            if sum(pov)>max(b):
                q += 1
print(q)


