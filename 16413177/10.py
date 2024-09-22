a = open("1011.txt")
q = 0
flag = 0
for i in a:
    b = [int(j) for j in i.split()]
    for k in range(len(b)):
        if b.count(b[k]) > 1:
            flag = 1
            break
    if flag == 0:
        if ((max(b)+min(b))/2) > ((sum(b)-max(b)-min(b))/4):
            q += 1
            print(b)
print(q)