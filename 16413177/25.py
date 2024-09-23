a = open("25.txt").readline()
res = 0
b = 2
set1 = {"Q", "R", "S"}
for i in range(0, len(a) - 2):
    set2 = {a[i], a[i+1], a[i+2]}
    if set1.issubset(set2) == True:
        res = max(res, b)
    else:
        b += 1
if {a[len(a)-3], a[len(a)-2], a[len(a)-1]} != {"Q", "R", "S"}:
    print(b)
else:
    print(res)#999493