for x in range(12):
    for y in range(12):
        n = int(f"{y}AA{x}", 12) + int(f"{x}02{y}", 14)
        if n % 80 == 0:
            print(n // 80)
