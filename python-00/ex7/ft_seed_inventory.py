def	ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
	name = seed_type.capitalize()
	match unit:
		case "packets":
			print(f"{name} seeds: {quantity} {unit} available")
		case "grams":
			print(f"{name} seeds: {quantity} {unit} total")
		case "area":
			print(f"{name} seeds: covers {quantity} square meters")
		case _:
			print("Unknown unit type")

if __name__ = "__main__":
	ft_seed_inventory()