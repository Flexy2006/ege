for N in range(1, 10000000):
    q2 = bin(N)[2:]
    if N % 5 == 0:
        q2 = q2 + bin(5)[2:]
    else:
        q2 = q2 + "1"
    if int(q2, 2) % 7 == 0:
        q2 = q2 + bin(7)[2:]
    else:
        q2 = q2 + "1"
    if int(q2, 2) < 1728404:
        print(int(q2, 2))


