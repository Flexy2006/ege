a = open("1001.txt")
x = 0
y = 1000000000
q = []
b = [int(i) for i in a]
for m in range(len(b)-1):
    if len(str(b[m])) == 3:
        if str(b[m])[-1] == "5":
            q.append(b[m])
for j in range(len(b)-1):
    if (len(str(b[j])) == 3 and len(str(b[j+1])) != 3) or (len(str(b[j+1])) == 3 and len(str(b[j])) != 3):
        if (b[j]+b[j+1]) % min(q) == 0:
            x += 1
            y = min(y, b[j]+b[j+1])
print(x,y)
        
