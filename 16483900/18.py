a = open("1002.txt")
x = 0
y = 0
b = [int(i) for i in a]
for j in range(len(b) - 1):
    for k in range(j + 1, len(b)):
        if (j*k)%10 == 0:
            x += 1
            y = max(y, (j+k))
print(x, y)