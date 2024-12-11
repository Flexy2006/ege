for n in range(4, 9999):
    q=0
    a = "5" + n*"2"
    while "52" in a or "1122" in a or "2222" in a:
        if "52" in a:
            a = a.replace("52", "11", 1)
        if "2222" in a:
            a = a.replace("2222", "5", 1)
        if "1122" in a:
            a = a.replace("1122", "25", 1)
    a = (" ".join(str(x) for x in a)).split()
    for i in a:
        q += int(i)
    if q == 64:
        print(n)
        break