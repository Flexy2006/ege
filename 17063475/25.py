for N in range(452022, 452300):
    q = []
    for i in range(2, N//2+1):
        if N % i == 0:
            q.append(i)
    q = sorted(q)
    if len(q) == 0:
        M = 0
    else:
        M = q[0]+q[-1]
    if M % 7 == 3:
        print(N, M)
