for A in range(300):
    b = 0
    for x in range(300):
        for y in range(300):
            if ((3*x+4*y) !=60) or ((A>=x) and (A>=y)):
                b += 1
    if b == 90000:
        print(A)
        break   