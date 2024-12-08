for A in range(10000):
    a = 0
    for x in range(10000):
        if ((x & 35 != 0) or (x & 22 != 0)) <= ((x & 15 == 0) <= (x & A != 0)):
            a += 1
    if a == 10000:
        print(A)#61
        break