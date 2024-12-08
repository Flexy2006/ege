for x in range(0, 8):
    for y in range(0, 8):
        n = int(f"{x}01{y}4", 9) + int(f"{x}{y}544", 8)
        if n % 89 == 0:
            print(n//89)