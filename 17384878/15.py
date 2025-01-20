for A in range(300):
    b = 0
    for x in range(300):
        for y in range(300):
            if (x*y < A) or (y > x) or (x >= 8):
                b += 1
    if b == 90000:
        print(A)
        break