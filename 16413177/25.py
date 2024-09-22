a = ["Q", "R", "S", "L", "W", "W"]
res = 0
b = 0
set1 = {"Q", "R", "S"}
for i in range(0, len(a) - 2):
    set2 = {a[i], a[i+1], a[i+2]}
    if set1.issubset(set2) == True:
        res = max(res, b)
    else:
        b += 1
print(res)#не до конца