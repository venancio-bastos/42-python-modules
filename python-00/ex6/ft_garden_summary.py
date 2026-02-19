def ft_garden_summary():
	try:
		garden_name = input("Enter garden name: ")
		total_plants = input("Enter number of plants: ")
		print(f"Garden: {garden_name}")
		print(f"Plants: {total_plants}")
		print("Status: Growing well!")
	except ValueError:
		print("Must be a number")

if __name__ == "__main__":
    ft_garden_summary()