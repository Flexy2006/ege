for x in "0123456789AB":
    for y in "0123456789AB":
        n = int(f"{x}231{y}", 12) + int(f"78{x}98{y}", 14)
        if n % 99 == 0:
            print(n // 99)
