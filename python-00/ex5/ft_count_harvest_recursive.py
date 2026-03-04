def ft_count_harvest_recursive(i=1, days_left=None):
    if days_left is None:
        days_left = int(input("Days until harvest: "))
        print(f"Day {i}")
    if i < days_left:
        i += 1
        ft_count_harvest_recursive(i, days_left)
    else:
        print("Harvest time!")
