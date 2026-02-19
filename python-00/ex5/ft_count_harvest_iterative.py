def	ft_count_harvest_iterative():
	try:
		days_left = int(input("Days until harvest: "))
		if days_left < 0:
			print("Must be a positive number")
			return
		for i in range (1, days_left + 1):
			print(f"Day {i}")
		print("Harvest time!")
	except ValueError:
		print("Must be a number")

if __name__ == "__main__":
    ft_count_harvest_iterative()