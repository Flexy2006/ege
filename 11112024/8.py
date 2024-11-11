from itertools import product
q = 0
for x in (product('0123', repeat=3)):
    if ((int(x[0]) + int(x[2])) > int(x[1])) and (x[0] != "0"):
        q += 1
print(q)