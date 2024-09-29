a = []
for N in range(4, 103):
    q2 = []
    N2 = N
    while N2 != 0:
        q = N2%2
        N2 = N2 // 2
        q2.append(q)
    q3 = q2[::]
    q3.pop(0)
    q3.pop(0)
    q3 = q3[::-1]
    q3 = "".join(str(i) for i in q3)
    q3 = int(q3, 2)
    if q2[0] == 0 and q2[1] == 1 and q3%2 == 0:
        a.append(N)
    if q2[0] == 1 and q2[1] == 0 and q3%2 == 1:
        a.append(N)
print(a[len(a)-1])#101


