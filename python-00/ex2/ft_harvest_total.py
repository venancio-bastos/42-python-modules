def ft_harvest_total():
    i = 1
    total = 0

    while i <= 3:
        number = int(input(f"Day {i} harvest: "))
        total += number
        i += 1
    print(f"Total harvest: {total}")
