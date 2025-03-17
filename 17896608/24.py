a = open('1002.txt').readlines()
m = 0
v = 0
for i in a:
    v += 1
    y = 0
    b = [j for j in i]
    q = 1
    for k in range(len(b)-1):
        if b[k] == b[k+1]:
            q += 1
        else:
            y = max(y,q)
            h = b[k-1]
            q = 1
    if m < y:
        m = y
        n_str = v
        let = h
    print(m)
print(a[n_str].count(let))


