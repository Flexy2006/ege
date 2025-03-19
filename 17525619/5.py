q = 0
for N in range(100,999):
    n = str(N)
    a = int(n[0])+int(n[1])
    b = int(n[1])+int(n[2])
    if a <= b:
        p = int(str(a)+str(b))
    else:
        p = int(str(b)+str(a))
    if p == 1216:
        q += 1
        print(N)
print(q)