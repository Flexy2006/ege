a = open('1001.txt')
a = a.readlines()
b = [int(i) for i in a]
q = 0
maxi = 0
maxi1 = 0
for x in range(len(b)):
    if str(b[x])[-1] == "9" and str(b[x])[-2] == "1":
        if maxi < b[x]:
            maxi = b[x]
for el in range(len(b) - 2):
    if (len(str(b[el])) == 4 and len(str(b[el+1])) == 4 and len(str(b[el+2])) != 4) or (len(str(b[el])) == 4 and len(str(b[el+1])) != 4 and len(str(b[el+2])) == 4) or (len(str(b[el])) != 4 and len(str(b[el+1])) == 4 and len(str(b[el+2])) == 4):
        if b[el] % 3 == 0 or b[el+1] % 3 == 0 or b[el+2] % 3 == 0:
            if b[el] + b[el+1] + b[el+2]  > maxi:
                print(b[el],b[el+1],b[el+2])
                if b[el]+b[el+1]+b[el+2] > maxi1:
                    maxi1 = b[el]+b[el+1]+b[el+2]
                q += 1
print(q, maxi1)