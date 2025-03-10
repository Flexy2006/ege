a = open("1001.txt")
res = []
x = 0
y = 0
b = [int(i) for i in a]
for i in b:
    if str(i)[-3:] == '321':
        res.append(i)
maxa = max(res)
for j in range(len(b)):
    for k in range(len(b)):
        for l in range(len(b)):
            if b[j] != b[k] != b[l]:
                if (len(str(b[j])) == 5 and len(str(b[l])) == 5 and len(str(b[k])) != 5) or (len(str(b[j])) == 5 and len(str(b[k])) == 5 and len(str(b[l])) != 5) or (len(str(b[k])) == 5 and len(str(b[l])) == 5 and len(str(b[j])) != 5):
                    if b[j] % 5 == 0 or b[l] % 5 == 0 or b[k] % 5 == 0:
                        if (b[j] + b[l] + b[k]) > maxa:
                            x += 1
                            y = max(y, b[j] + b[k] + b[l])
print(x, y)