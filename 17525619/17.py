a = open('1001.txt')
b = [int(i) for i in a]
x = 0
y = 0
ar13 = []
for k in b:
    if len(str(k)) >= 2:
        if str(k)[-1] == '3' and str(k)[-2] == '1':
            ar13.append(k)
for j in range(0,len(b)-2):
    if (len(str(b[j])) == 3 and len(str(b[j+1])) == 3 and len(str(b[j+2])) != 3) or (len(str(b[j])) == 3 and len(str(b[j+1])) != 3 and len(str(b[j+2])) == 3) or (len(str(b[j])) != 3 and len(str(b[j+1])) == 3 and len(str(b[j+2])) == 3):
        if (b[j]+b[j+1]+b[j+2]) <= max(ar13):
            x += 1
            y = max(y,b[j]+b[j+1]+b[j+2])
print(x,y)