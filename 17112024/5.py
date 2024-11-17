q = []
for N in range(456789000, 456789012):
    n = bin(N)[2:]
    if N % 2 == 0:
        n = "11" + n
    else:
        n = "1" + n + "10"
    q.append(int(n, 2))
print(max(q))