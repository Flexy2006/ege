for n in range(4, 100):
    k = "1"+n*"2"
    q = 0
    while '12' in k or '322' in k or '222' in k:
        if '12' in k:
            k = k.replace('12', '2', 1)
        if '322' in k:
            k = k.replace('322', '21', 1)
        if '222' in k:
            k = k.replace('222', '3', 1)
    k = int(k)
    while k > 0:
        q += k % 10
        k //= 10
    if q == 15:
        print(n)
        break
