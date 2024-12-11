a = open('1002.txt')
b = a.readline()
maxi = 0
signs = "-*"
num = "123456"
n = 0
for j in range(1, len(b)):
    if b[j] == "B" and n == 0:
        n += 1
    elif n > 0 and (b[j] in num or ((b[j] in signs) and (b[j-1] not in signs))):
        n += 1
    else:
        maxi = max(maxi, n)
        n = 0 
maxi = max(maxi, n)
print(maxi)