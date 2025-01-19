q = []
m = 0
for N in range(1, 100):
    n = N
    k = []
    while n > 0:
        k.append(n%3)
        n //= 3
    k = k[::-1]
    k = "".join(str(x) for x in k)
    if N % 3 == 0:
        k += k[-2]
        k += k[-2]
    else:
        m = int(k)
        l = 0
        while m > 0:
            l += (m % 10)
            m //= 10
        g = []
        while l > 0:
            g.append(l%3)
            l //= 3
        g = g[::-1]
        g = "".join(str(x) for x in g)
        k += g
    R = int(k, 3)
    if R > 220 and R % 2 == 0:
        q.append(R)
print(min(q))
    
