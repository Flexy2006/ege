for x in range(1, 20):
    p = 3**100-x
    q = 0
    while p > 0:
        if p % 3 == 0:
            q += 1
        p //= 3
    if q == 2:
        print(x)
        break