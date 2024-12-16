a = open("1001.txt")
x = 0
y = 111111111111111111
q = []
b = [int(i) for i in a]
for m in b:
    if len(str(m)) >= 2:
        if str(m)[-1] == "4" and str(m)[-2] == "2":
            q.append(m)
for j in range(len(b)-2):
    if (len(str(b[j])) == 3 and len(str(b[j+1])) != 3 and len(str(b[j+2])) != 3) or (len(str(b[j])) != 3 and len(str(b[j+1])) == 3 and len(str(b[j+2])) != 3) or (len(str(b[j])) != 3 and len(str(b[j+1])) != 3 and len(str(b[j+2])) == 3):
        if b[j]+b[j+1]+b[j+2] > max(q):
            x += 1
            y = min(y, b[j]+b[j+1]+b[j+2])
print(x,y)
        
