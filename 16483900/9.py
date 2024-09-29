from itertools import product
words = list(product("ЗИМА", repeat=5))
q = 0
for x in words:
    if x.count("З") + x.count("А") == 1:
        q += 1
print(q)#160