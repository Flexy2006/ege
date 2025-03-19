from fnmatch import *
import math
q = 0
for N in range(110250000,110300001):
    q = []
    for i in range(2,int(math.sqrt(N))+1):
        if N % i == 0:
            q.append(i)
        if len(q) == 2:
            break
    if len(q) != 2:
        M = 0
    else:
        M = N//int(q[0])+N//int(q[1])
    if fnmatch(str(M),'*1002'):
        print(N)
        