a = open("1001.txt")
x = 0
y = 0
q = []
b = [int(i) for i in a]
for m in b:
    if str(m)[-1] == "7" and str(m)[-2] == "1":
        q.append(m)
for j in range(len(b)-2):
    if (len(str(b[j])) == 4 and len(str(b[j+1])) == 4 and len(str(b[j+2])) != 4) or (len(str(b[j])) == 4 and len(str(b[j+1])) != 4 and len(str(b[j+2])) == 4) or (len(str(b[j])) != 4 and len(str(b[j+1])) == 4 and len(str(b[j+2])) == 4):
        if b[j] % 5 == 0 or b[j+1] % 5 == 0 or b[j+2] % 5 == 0:
            if b[j]+b[j+1]+b[j+2] > max(q):
                x += 1
                y = max(y, b[j]+b[j+1]+b[j+2])
print(x,y)
        
