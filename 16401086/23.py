a = open("1003.txt").readline()
q = 1
l = 0
for i in range(len(a) - 1):
    if a[i] not in 'ABC' or a[i+1] not in 'ABC':
        q += 1
    else:
        l = max(l, q)
        q = 1
print(l)#49