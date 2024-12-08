a = open('1002.txt')
b = a.readline()
maxi = 0
let = "QRW"
num = "124"
n = 1
for j in range(len(b)- 1):
    if (b[j] in let and b[j+1] in num) or (b[j] in num and b[j+1] in let):
        n += 1
    else:
        maxi = max(maxi, n)
        n = 1
print(maxi)