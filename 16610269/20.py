a = [int(i) for i in open("1003.txt").readlines()]
x = 0
y = 0
b = []
for i in a:
    if i % 19 == 0:
        b.append(i)
c = min(b)
for i in range(len(a) - 1):
    if (a[i] % c == 0) or (a[i+1] % c == 0):
            x += 1
            y = max(y, (a[i] + a[i+1]))
print(x, y)#142 175430