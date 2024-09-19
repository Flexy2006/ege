a = open('1000.txt')
q = 0
q1 = 0
q2 = 0
for i in a:
    yes = []
    no = []
    b = [int(j) for j in i.split()]
    for k in b:
        if b.count(k) == 1:
            no.append(k)
        else:
            yes.append(k)
    if len(no)>0 and len(yes)>0:
        for l in range(len(no)):
            q1 += int(no[l])
        for m in range(len(yes)):
            q2 += int(yes[m])
        if (q1//len(no))>(q2//len(yes)):
            q += 1
        q1 = 0
        q2 = 0
print(q)#2065   