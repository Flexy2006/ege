a = open('1002.txt')
b = a.readline()
mini = 1000000000
p = []
n = 0
for i in range(len(b) - 1):
    if b[i] == "T":
        p.append(i)
for j in range(1, len(p)- 209):
    n = p[j + 209] - p[j] + 1
    if n < mini:
        mini = n
print(mini)