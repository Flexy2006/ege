q = []
m = 0
for N in range(1, 1000):
    R = bin(N)[2:]
    R += bin(N % 4)[2:]
    q.append(int(R, 2))
for i in range(1, 1000-64):
    l = 0
    for j in range(i, i+64):
        if j in q:
            l += 1
    m = max(m, l)
print(m, sorted(q)) #+5 +11
