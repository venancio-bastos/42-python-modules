def	ft_plot_area():
	try:
		length = int(input("Enter length: "))
		width = int(input("Enter width: "))
		if length <= 0 or width <= 0:
			print("Error: Values must be positive number")
			return
		total = length * width
		print(f"Plot area: {total}")
	except ValueError:
		print("Error: Must be a number")

if __name__ == "__main__":
    ft_plot_area()