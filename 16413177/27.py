import math
p = []
f = open("27.txt")
n = int(f.readline())
s = 0
maxi = 0
for i in f:
    m = int(i)
    if m <= 100:
        s += m
    else:
        p.append(m)
p.sort()
for i in range(len(p)):
    if i < len(p) // 2:
        s += p[i] * 7 / 10
        maxi = p[i]
    else:
        s += p[i]
print(math.ceil(s), maxi)