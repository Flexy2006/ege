q = 0
from itertools import *
for x in product("БОРИС", repeat=6):
    if (x.count('Б') == 1 and x.count('Р') == 1) and (x.count("С")== 0 or x.count("С") == 1):
        q +=1
print(q)