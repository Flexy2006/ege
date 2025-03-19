a = open('1002.txt').readline()
q = 0
y = 0
for i in range(len(a)):
    if a[i] in 'ABCDEFGHIJKLMNOP':
        q += 1
    else:
        y = max(y,q)
        q = 0
print(y)