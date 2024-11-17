a = open("1002.txt")
b = [int(i) for i in a]
b = sorted(b)
t = []
t.append(b[0])
for j in b:
    if j >= t[-1] + 4:
        t.append(j)
print(len(t), b[0])