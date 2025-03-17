a = open('1000.txt')
q = 0
for i in a:
    b = [int(j) for j in i.split()]
    zam = []
    ch1 = []
    nech1 = []
    ch = []
    nech = []
    for k in b:
        if k > (sum(b) / len(b)):
            zam.append(k)
        if k % 2 == 0:
            ch.append(k)
        else:
            nech.append(k)
    for x in zam:
        if x%2 == 0:
            ch1.append(x)
        else:
            nech1.append(x)
    if len(ch1) > len(nech1):
        if sum(nech) > sum(ch):
            q += 1
print(q)
