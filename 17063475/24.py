a = open('1002.txt')
b = a.readline()
maxi = 0
for j in range(len(b)):
    n = 0
    q1 = 0
    q2 = 0
    for k in range(j, len(b)):
        n += 1
        if b[j] == "A":
            q1 += 1
        if b[j] == "B":
            q2 += 1
        if (q1 > 1 and q2 == 1) or (q2 > 1 and q1 == 1):
            maxi = max(maxi, n)
print(maxi)