a = open('1004.txt').readline().split('A')
q = 0
for x in a:
    if not('B') in x and len(x) >= 10:
        q += 1
print(q)#9428