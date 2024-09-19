a = open('1004.txt').readline()
q = 3
l = 0
for i in range(len(a) - 3):
    if a[i] == "X" and a[i + 1] == "Z" and a[i + 2] == "Z" and a[i + 3] == "Y":
        l = max(l, q)
        q = 3
    else:
        q += 1
print(l)#1713