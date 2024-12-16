res = 0
for i in range(1, 9):
    for j in range(0, 9):
        for k in range(0, 9):
            for l in range(0, 9):
                for m in range(0, 9):
                    a = str(i) + str(j) + str(k) + str(l) + str(m)
                    if a.count('5') == 1:
                        if a.index('5') != 4 and a.index('5') != 0:
                            if int(a[a.index('5') + 1]) % 2 == 0 and int(a[a.index('5') - 1]) % 2 == 0:
                                res += 1
                        elif a.index('5') == 0:
                            if int(a[a.index('5') + 1]) % 2 == 0:
                                res += 1
                        elif a.index('5') == 4:
                            if int(a[a.index('5') - 1]) % 2 == 0:
                                res += 1
print(res)