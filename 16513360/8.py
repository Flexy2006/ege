a = open('8.txt')
b = 0
for i in a:
    c = [int(j) for j in i.split()]
    for x in c:
        if c.count(x) == 3 and len(set(c)) == 4:
            if (3*x)**2 > (sum(c) - 3*x)**2:
                b += 1
print(b//3)