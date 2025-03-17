for N in range(100,999):
    n = str(N)
    a = int(n[0])+int(n[1])
    b = int(n[1])+int(n[2])
    if a > b:
        c = str(a)+str(b)
    else:
        c = str(b)+str(a)
    if c == "159":
        print(N)
        break