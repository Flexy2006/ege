a = open('1003.txt')
b = a.readline()
maxi = 0
p = []
n = 0
for i in range(len(b) - 1):
    if b[i] == "C" and b[i+1] == "D":
        p.append(i)
for j in range(1, len(p)- 142):
    n = p[j + 142] - p[j] - 1
    if n > maxi:
        maxi = n
print(maxi)