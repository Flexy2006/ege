a = open('1001.txt')
b = [int(i) for i in a]
x = 0
y = 0
for k in range(1,len(b)):
    for l in range(k+1, len(b)):
        if abs(b[k]-b[l])%60==0 and (b[k]%15==0 or b[l]%15==0):
            x += 1
            y = max(y,abs(b[k]-b[l]))
print(x,y)