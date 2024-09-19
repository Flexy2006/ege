from itertools import product
q = 0
a = list(product('АВЛОР', repeat = 4))
for i in a:
    q += 1
    if i[0] == "Л":
        break
print(q)#251