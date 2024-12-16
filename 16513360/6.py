a = open('6.txt')
b = 0
for i in a:
    c = [int(j) for j in i.split()]
    d = c.sort()
    if c[2] ** 2 < c[0] ** 2 + c[1] ** 2:
        b += 1
print(b)