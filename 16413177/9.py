a = open('1000.txt')
b = 0
for i in a:
    c = [int(j) for j in i.split()]
    if c.count(max(c)) == 1:
        if len(set(c)) < len(c):
            if max(c) > ((sum(c) - max(c))/5)*3:
                b += 1
print(b)