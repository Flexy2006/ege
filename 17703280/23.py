for A in range(300):
    b = 0
    for x in range(300):
        for y in range(300):
            if (x + 2*y > 48)or(y>x)or(x+3*y < A):
                b += 1
    if b != 90000:
        print(A)
 