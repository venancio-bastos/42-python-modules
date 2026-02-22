def	ft_water_reminder():
	days = int(input("Days since last watering: "))
	if days < 0:
		print("Must be a positive number")
		return
	if days > 2:
		print("Water the plants!")
	else:
		print("Plants are fine")