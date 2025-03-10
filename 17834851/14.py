for x in range(1, 9):
    x = str(x)
    M = int(f'842{x}5', 9)
    N = int(f'8{x}725', 9)
    for A in range(1, 1000):
        if (int(M) + A) % int(N) == 0:
            print(A, x)
            break