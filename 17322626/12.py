p = []
for N in range(3, 100):
    k = '1'*N
    while '111' in k:
        k = k.replace('111', '2', 1)
        k = k.replace('222', '11', 1)
        k = k.replace('1', '2', 1)
    if k.count("2") == len(k):
        p.append(N)
print(p)#повторяется, считаем на пальцах
