for N in range(1, 1000):
    q = format(N, 'b')
    if q.count('1') % 2 == 0:
        q += "0"
    else:
        q += "1"
    R = int(q, 2)
    if R > 97:
        print(R)#99
        break