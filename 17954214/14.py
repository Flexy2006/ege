for x in '0123456789ABCDE':
    M = int(f'123{x}5', 15)
    N = int(f'1{x}233', 15)
    if (M + N) % 14 == 0:
        print((M + N) // 14)