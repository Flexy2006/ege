a = open('113.txt')
q = 0
for i in a:
    b = [int(j) for j in i.split()]
    #c = " ".join(str(k) for k in b)
    #d = c.sort()
    flag1 = 0
    flag2 = 0
    b.sort()
    #print(b)
    if int(b[3]) - int(b[2]) == int(b[2]) - int(b[1]) == int(b[1]) - int(b[0]):
        flag1 = 1
        #print(b)
    f = 1
    w = b[3]
    b.pop(3)
    for x in b:
        f *= x
    if w**2 > f:
        flag2 = 1
        #print(b)
    if flag1 == flag2 == 1:
        q += 1
        #print(b, w, w**2, f)
print(q)
