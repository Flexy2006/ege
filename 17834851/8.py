q = 0
from itertools import *
for x in product("АНДРЕЙ", repeat=6):
    if x.count("А") >= 1 and x.count("Й") <= 1:
        q += 1
print(q)