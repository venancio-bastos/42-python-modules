class Plant:
	"""
	Plant objects.
	"""
	def __init__(self, name: str, height: float, age: int) -> None:
		"""
        Plant object constructs.
        """
		self.name = name
		self.height = height
		self.age = age

def plant_factory() -> list[Plant]:
	"""
    Creates multiple plants returns a list.
    """
	plants = [
		("Rose", 25, 30),
		("Oak", 200, 365),
		("Cactus", 5, 90),
		("Sunflower", 80, 45),
		("Fern", 15, 120)
	]
	total_plants = []
	for name, height, age in plants:
		new_plant = Plant(name, height, age)
		print(f"Created: {new_plant.name} ({new_plant.height}cm, {new_plant.age} days)")
		total_plants.append(new_plant)
	return total_plants
	
def main() -> None:
	"""
	Generate plants and print them.
	"""
	print("=== Plant Factory Output ===")
	plants = plant_factory()
	print(f"\nTotal plants created: {len(plants)}")

if __name__ == "__main__":
	main()