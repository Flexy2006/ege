for x in range(0, 8):
    for y in range(0, 8):
        n = int(f"88{x}4{y}", 9) + int(f"7{x}44{y}", 11)
        if n % 61 == 0:
            print(n//61)