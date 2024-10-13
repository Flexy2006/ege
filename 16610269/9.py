from itertools import product
q = 0
words = list(product('012345678', repeat=5))
for x in words:
    if x[0] > x[1] > x[2] > x[3] > x[4] and x[0] != 0:
        q += 1
print(q)#126