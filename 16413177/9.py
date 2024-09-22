a = open("1010.txt")
q = 0
flag = 0
for i in a:
    b = [int(j) for j in i.split()]
    if b.count(max(b)) == 1:
        for k in range(len(b)):
            if b.count(b[k]) > 1:
                flag = 1
                break
        if flag == 1:
            if max(b) > (sum(b)-max(b))/5 * 3:
                q += 1
print(q)#561