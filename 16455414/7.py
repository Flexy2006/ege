q = []
for i in range(1000, 10000):
    i = str(i)
    a = []
    a.append(str(int(i[0])+int(i[1])))
    a.append(str(int(i[1])+int(i[2])))
    a.append(str(int(i[2])+int(i[3])))
    b = a.sort(reverse=True)
    if (a[1] + a[0]) == "1315":
        q.append(i)
print(max(q))#9676