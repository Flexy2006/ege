count_del = 0
i = 800000
while count_del < 5:
    i += 1
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            if i / j == i:
                break
            if (i / j + j) % 10 == 4:
                print(i, i // j + j)
                count_del += 1
            break