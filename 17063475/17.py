a = open("1001.txt")
x = 0
y = 0
q = []
b = [int(i) for i in a]
for m in b:
    if len(str(m)) >= 3:
        if str(m)[-1] == "3" and str(m)[-2] == "2" and str(m)[-3] == "1":
            q.append(m)
for j in range(len(b)-2):
    if (len(str(b[j])) == 5 and len(str(b[j+1])) == 5) or (len(str(b[j+1])) == 5 and len(str(b[j+2])) == 5) or (len(str(b[j])) == 5 and len(str(b[j+2])) == 5):
        if (b[j] % 3 == 0 and b[j+1] % 3 != 0 and b[j+2] % 3 != 0) or (b[j] % 3 != 0 and b[j+1] % 3 == 0 and b[j+2] % 3 != 0) or (b[j] % 3 != 0 and b[j+1] % 3 != 0 and b[j+2] % 3 == 0):
            if b[j]+b[j+1]+b[j+2] > max(q):
                x += 1
                y = max(y, b[j]+b[j+1]+b[j+2])
print(x,y)
        
