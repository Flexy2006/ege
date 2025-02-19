a = open('1000.txt')
q = 0
for i in a:
    b = [int(j) for j in i.split()]
    if b[0]+b[1]>b[2] and b[2]+b[1]>b[0] and b[0]+b[2]>b[1]:
        q += 1
print(q) 