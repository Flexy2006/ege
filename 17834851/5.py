for N in range(100, 1000):
    n = str(N)
    m = int(n[0]) + int(n[1])
    k = int(n[1]) + int(n[2])
    q = str(min(m, k)) + str(max(m, k))
    if q == '714':
        print(N)
        break