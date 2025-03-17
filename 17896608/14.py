P = [i for i in range(10, 30)]
Q = [i for i in range(13, 19)]
m = 0
for Amin in range(0, 100):
    for Amax in range(Amin + 1, 100):
        check = 1
        A = [i for i in range(Amin, Amax)]
        for x in range(-200, 200):
            f = ((x in A) <= (x in P)) or (x in Q)
            if not f:
                check = 0
                break
        if check == 1:
            m = max(m,Amax - Amin)
print(m - 1)