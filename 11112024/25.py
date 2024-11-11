for n in range(700000, 100000000):
    i = 2
    p = []
    while i < n:
        if n % i == 0:
            p.append(i)
        i += 1
    if len(p) < 2:
        x = 0
    else:
        x = p[0] + p[-1]
    if str(x)[-1] == "4":
        print(n)
    
