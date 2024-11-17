for x in range(0, 8):
    for y in range(0, 8):
        n = int(f"{y}04{x}5", 11) + int(f"253{x}{y}", 8)
        if n % 117 == 0:
            print(n//117)