a = open("1001.txt")
x = 0
y = 0
q = 0
b = [int(i) for i in a]
for i in range(len(b)):
    if b[i] % 32 == 0:
        q += 1
for j in range(len(b) - 1):
    if b[j] < 0 or b[j+1] < 0:
        if b[j] + b[j+1] < q:
            x += 1
            y = max(y, b[j] + b[j+1])
print(x, y)