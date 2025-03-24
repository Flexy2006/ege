q = []
for N in range(1,1000):
    n = bin(N)[2:]
    if N % 2 == 0:
        n += '01'
    else:
        n += '10'
    R = int(n,2)
    if R > 102:
        print(N)
        break
