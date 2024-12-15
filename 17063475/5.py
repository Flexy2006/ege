for n in range(1000, 10000):
    n = str(n)
    a1 = int(n[0])+int(n[1])
    a2 = int(n[1])+int(n[2])
    a3 = int(n[2])+int(n[3])
    p = [a1, a2, a3]
    p.remove(min(a1,a2,a3))
    p = sorted(p)
    R = int(str(p[0]) + str(p[1]))
    if R == 1215:
        print(n)
        break
    
    