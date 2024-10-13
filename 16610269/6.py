a = []
for N in range(4, 100003):
    q2 = []
    N2 = N
    while N2 != 0:
        q = N2%2
        N2 = N2 // 2
        q2.append(q)
    q3 = q2[::]
    q3.pop(0)
    if N % 2 == 0:
        q3.append("0")
        q3.append("1")
    else:
        q3.append("1")
        q3.append("0")
    q3 = q3[::-1]
    q3 = "".join(str(i) for i in q3)
    q3 = int(q3, 2)
    if q3 == 2018:
        print(N)#1989


