for A in range(300):
    a = 0
    for x in range(1,301):
        for y in range(1,301):
            if (x - 3*y < A) or (y > 400) or (x > 56):
                a += 1
    if a == 300*300:
        print(A)
        break