for A in range(300):
    b = 0
    for x in range(300):
        for y in range(300):
            if ((x&57 > 0)or(x&99 > 0)) <= (x&A > 0):
                b += 1
    if b == 90000:
        print(A)
        break   