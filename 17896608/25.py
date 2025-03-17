import math
for n in range(45000000,50000001):
    x = n
    g = []
    if n % 2 == 0:
        w = 1
    else:
        w = 2
    for i in range(2,int(math.sqrt(x))+1):
        q = 0
        while x % i == 0:
            x //= i
            q += 1
        g.append(q)
    o = []
    for p in range(len(g)):
        if p % 2 == 1:
            o.append(g[p])
    w += sum(o)
    for l in range(len(o)-1):
        for b in range(l+1, len(o)):
            w += o[l]*o[b]
    print(n,w,o)
