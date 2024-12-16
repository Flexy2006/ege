a = open("25.txt").readline()
maxi = 1
n = 1
for i in range(len(a) - 1):
    if a[i] not in "QRS" or a[i+1] not in "QRS":
        n+=1
        maxi = max(maxi, n)
    else:
        n = 1
print(maxi)
