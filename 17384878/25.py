from fnmatch import fnmatch
n = 1095421
n += 3023 - n % 3023

for x in range(n, 10**10, 3023):
    if fnmatch(str(x), '1?954*21'):
        print(x)