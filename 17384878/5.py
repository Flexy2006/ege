for N in range(1,100):
    n = list(bin(N)[2:])
    n = n[::-1]
    for m in n:
        if m == "0":
            n.remove(m)
    n = "".join(str(x) for x in n)
    R = int(n, 2)
    if R == 13:
        print(N)
