a = open('1002.txt')
b = [int(x) for x in a]
c = set()
q = 0
for i in range (0, 9998):
    for j in range(i+1, 9999):
        if (i + j)%80 == 0:
            if i%50 == 0 or j%50 == 0:
                c.add(i+j)
                q += 1
print(q, c)

