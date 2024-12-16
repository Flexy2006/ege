a = open('7.txt')
b = 0
for i in a:
    c = [int(j) for j in i.split()]
    d = c.sort()
    if len(set(c)) == 6 and (c[5] + c[0])/2 > sum(c)/6:
        b += 1
print(b)