a = open('1001.txt')
m = []
m2 = []
with open("1001.txt") as f:
    for s in f:
        s = list(map(int, s.split()))
        m.append(s)
m2 = sum(m, [])
q = 0
for i in a:
    b = [int(j) for j in i.split()]
    for k in range(len(b)):
        if b.count(b[k]) == 1:
            if m2.count(b[k]) == 45:
                q += 1
                break
print(q)#690