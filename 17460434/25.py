from fnmatch import fnmatch
n = 1423907
n += 3147 - n % 3147

for x in range(n, 10**10, 3147):
    if fnmatch(str(x), '1*4239?7'):
        print(x)