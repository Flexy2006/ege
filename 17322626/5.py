p = []
for N in range(1, 100):
    n = str(bin(N)[2:])
    q = 0
    k = str(int(n, 2))
    for i in range(len(k)):
        q += int(k[i])
    if q % 2 != 0:
        n += '1'
    else:
        n += '0'
    k = str(int(n, 2))
    q = 0
    for i in range(len(k)):
        q += int(k[i])
    if q % 2 != 0:
        n += '1'
    else:
        n += '0'
    k = str(int(n, 2))
    q = 0
    for i in range(len(k)):
        q += int(k[i])
    if q % 2 != 0:
        n += '1'
    else:
        n += '0'
    p.append(int(n, 2))
print(p)

    
    
