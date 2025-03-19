for A in range(500):
    q = 0
    for x in range(300):
        for y in range(300):
            if ((y+2*x) != 48) or (A < x) or (A < y):
                q += 1
    if q == 300*300:
        print(A)