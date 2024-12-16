for i in range(100,1000):
    a = list(map(int, str(i)))
    b = a[1] + a[2]
    c = a[0] + a[1]
    p = [b,c]
    p = sorted(p)
    g = str(p[0])+str(p[1])
    if g == "714":
        print(i)#770
        break