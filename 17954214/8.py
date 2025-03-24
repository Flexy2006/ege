from itertools import *
q = 0
s = 'ЗМ'
g = 'ИА'
for x in product('ЗИМА',repeat=5):
    if x[0] in s and x[4] in g:
        q += 1
print(q)
