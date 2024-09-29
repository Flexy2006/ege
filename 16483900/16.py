for A in range(1000):
    a = 0
    for x in range(1000):
        for y in range(1000):
            if ((x + 2*y) < A) or (y > x) or (x > 20):
                a += 1
    if a == 1000000:
        print(A)#61
        break