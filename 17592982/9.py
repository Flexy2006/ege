q = []
for N in range(568023,569231):
    w = 0
    for i in range(1,N//2+1):
        if N % i == 0:
            w += 1
    q.append(w+1)
print(max(q), q.index(max(q))+568023)