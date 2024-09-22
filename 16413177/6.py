for i in range(100,1000):
    a = list(map(int, str(i)))
    b = str(a[1] + a[2]) + str(a[0] + a[1])
    if b == "714":
        print(i)#770
        break