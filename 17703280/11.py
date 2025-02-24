q = 0
from itertools import *
for x in product("КОНФЕТА", repeat=5):
    if x.count("Е") == 2 and x[1] != "Ф":
        q +=1
print(q)