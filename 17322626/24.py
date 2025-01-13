f = open('24.txt')
a = [x for x in f.readlines()]
max_s = 0
for i in range(len(a)):
    if a[i].count('A') < 25:
        for j in range(len(a[i])-1):
            for q in range(j+1, len(a[i])):
                if a[i][j] == a[i][q]:
                    if abs(j - q) > max_s:
                        max_s = abs(j - q)
print(max_s)