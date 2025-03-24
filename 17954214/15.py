for A in range(1, 300):
    k = 0
    for m in range(0, 300):
        for n in range(0, 300):
            if (3*m + 4*n > 66) or (m <= A) or (n < A):
                k += 1
    if k == 90000:
        print(A)
        break