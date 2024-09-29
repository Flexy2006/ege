a = open('1000.txt')
q = 0
for i in a:
    b = [int(j) for j in i.split()]
    if len(set(b)) == len(b):
        if (max(b)+min(b))/2 > (sum(b)-max(b)-min(b))/4:
            q += 1
print(q)#6840