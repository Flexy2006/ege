a = open("1001.txt")
x = 0
y = 0
q = []
b = [int(i) for i in a]
for j in range(len(b)):
    for k in range(len(b)):
        if j != k:
            if (b[j]-b[k])%2 == 0 and (b[j] % 31 == 0 or b[k] % 31 == 0):
                x += 1
                y = max(y, b[j]+b[k])
print(x/2,y)
        
