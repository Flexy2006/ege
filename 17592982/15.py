a = open('1003.txt')
b = [int(i) for i in a]
x = 0
y = 0
mini = min(b)
maxi = max(b)
for j in range(0,len(b)-2):
    if len(str(b[j])) == 4 or len(str(b[j+1])) == 4 or len(str(b[j+2])) == 4:
        if (b[j] % 5 == mini % 5 and b[j+1] % 5 != mini % 5 and b[j+2] % 5 != mini % 5) or (b[j+1] % 5 == mini % 5 and b[j+2] % 5 != mini % 5 and b[j] % 5 != mini % 5) or (b[j+2] % 5 == mini % 5 and b[j] % 5 != mini % 5 and b[j+1] % 5 != mini % 5) or (b[j] % 5 != mini % 5 and b[j+1] % 5 != mini % 5 and b[j+2] % 5 != mini % 5):
            if (b[j] % 7 == maxi % 7 and b[j+1] % 7 == maxi % 7 and b[j+2] % 7 != maxi % 7) or (b[j+1] % 7 == maxi % 7 and b[j+2] % 7 == maxi % 7 and b[j] % 7 != maxi % 7) or (b[j+2] % 7 == maxi % 7 and b[j] % 7 == maxi % 7 and b[j+1] % 7 != maxi % 7) or (b[j] % 7 == maxi % 7 and b[j+1] % 7 == maxi % 7 and b[j+2] % 7 == maxi % 7):
                x += 1
                y = max(y,b[j]+b[j+1]+b[j+2])
print(x,y)