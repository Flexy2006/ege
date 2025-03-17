a = '0'+18*'1'+11*'2'+7*'3'+'0'
while not('00') in a:
    a = a.replace('01','210',1)
    a = a.replace('02','3101',1)
    a = a.replace('03','2012',1)
print(a.count('1'),a.count('2'),a.count('3'))#61x1, 50x2, 18x3
#+3: +3 +3 +1
#+2: +2 +1 +1
#+1: +1 +1 +0
for x in range(100):
    for y in range(100):
        for z in range(100):
            if (3*x+2*y+z) == 61 and (3*x+y+z) == 50 and (x+y) == 18:
                print(x,y,z)
                break