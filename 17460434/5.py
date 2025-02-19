l = []
for N in range(1,500):
    n = list(bin(N)[2:])
    q = 0
    for m in n:
        q+=int(m)
    n+=str(q%2)
    q = 0
    for m in n:
        q+=int(m)
    n+=str(q%2)
    n = "".join(str(x) for x in n)
    R = int(n, 2)
    if R > 123:
        l.append(R)
print(min(l))

