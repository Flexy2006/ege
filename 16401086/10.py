a = open('1001.txt')
q = 0
flag = 0
for i in a:
    b = [int(j) for j in i.split()]
    if b.count(min(b)) == 1:
        for k in b:
            if b.count(k)>1:
                flag = 1
                break
        if flag == 1:
            if (3*((sum(b)-max(b))/5)) < max(b):
                q += 1
print(q)#515
