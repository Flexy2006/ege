for A in range(1000):
    q = 0
    for n in range(1000):
        for m in range(1000):
            if (3 * m + 4 * n > 63) or ((m <= A) or (n < A)):
                q += 1
    if q == 1000000:
        print(A)#9
        break