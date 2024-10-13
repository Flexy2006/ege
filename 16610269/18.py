for A in range(1000):
    a = 0
    for x in range(1000):
        for y in range(1000):
            if (x<A) or (y<A) or ((x+2*y)>50):
                a += 1
    if a == 1000000:
        print(A)#17
        break