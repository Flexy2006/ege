from itertools import *
q = 0
for x in product(sorted('QWERTYUIOPASDFGHJKLZXCVBNM'), repeat=1):
    q += 1
for x in product(sorted('QWERTYUIOPASDFGHJKLZXCVBNM'), repeat=2):
    q += 1
for x in product(sorted('QWERTYUIOPASDFGHJKLZXCVBNM'), repeat=3):
    q += 1
for x in product(sorted('QWERTYUIOPASDFGHJKLZXCVBNM'), repeat=4):
    q += 1
for x in product(sorted('QWERTYUIOPASDFGHJKLZXCVBNM'), repeat=5):
    q += 1
for x in product(sorted('QWERTYUIOPASDFGHJKLZXCVBNM'), repeat=6):
    if x == "FDECBA":
        print(q)
        break
    q += 1
print(q)