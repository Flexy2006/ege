#72559
from itertools import *
t="12 13 14 21 25 27 31 34 37 41 43 48 52 56 58 65 68 72 73 84 85 86"
g="AF FA FG GF AG GA GD DG FH HF DE ED BE EB BD DB EH HE CB BC CH HC"

s=set(g.replace(' ',''))
for p in permutations(s):
    nt=t
    for i,v in enumerate(p):
        nt=nt.replace(str(i+1),v)
    if set(g.split())==set(nt.split()):
        print (p)