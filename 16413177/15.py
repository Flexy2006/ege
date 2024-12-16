for x in range(0, 12):
    n = int(f"28{x}2", 18) + int(f"93{x}5",12)
    if n % 133 == 0:
        print(n//133)