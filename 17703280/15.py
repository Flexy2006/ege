q = 0
from itertools import *
for x in product(sorted("ОЛЬГА"), repeat=5):
    q += 1
    if ''.join(str(i) for i in x) == "ОЛЬГА":
        print(q)
        break