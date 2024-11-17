a = open("1001.txt")
x = 0
y = 0
b = [int(i) for i in a]
mini = min(b) % 3
maxi = max(b) % 7
for j in range(len(b) - 1):
    if b[j] % 3 == mini or b[j+1] % 3 == mini:
        if b[j] % 7 == maxi or b[j+1] % 7 == maxi:
            x += 1
            y = max(y, (b[j]+b[j+1]))
print(x, y)