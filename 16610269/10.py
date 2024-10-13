a = open('1000.txt')
q = 0
for i in a:
    b = [int(j) for j in i.split()]
    yes = []
    no = []
    if len(set(b)) == len(b):
        for x in b:
            if x % 2 == 0:
                yes.append(x)
            else:
                no.append(x)
        if len(yes) > len(no):
            if sum(yes) < sum(no):
                q += 1
print(q)#241