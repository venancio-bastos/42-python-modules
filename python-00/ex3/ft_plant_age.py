def ft_plant_age():
	try:
		plant_age = int(input("Enter plant age in days: "))
		if plant_age < 0:
			print("Must be a positive number")
			return
		if plant_age > 60:
			print("Plant is ready to harvest!")
		else:
			print("Plant needs more time to grow.") 
	except ValueError:
		print("Must be a number!")

if __name__ == "__main__":
    ft_plant_age()