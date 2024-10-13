a = open('1001.txt')
q = 0
for i in a:
    b = [int(j) for j in i.split()]
    if len(set(b)) == len(b):
        if max(b) < (sum(b) - max(b)):
            q += 1
print(q)#13189