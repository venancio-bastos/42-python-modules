#!/usr/bin/env python3

class Plant:
	"""
	Acts as a blueprint for Plant objects.
	"""
	def __init__(self, name: str, height: float, age: int) -> None:
		"""
        Constructs a Plant object.
        """
		self.name = name
		self.height = height
		self.age = age
	
	def __str__(self) -> str:
		"""
		Returns a readable string representation of the plant.
		"""
		return f"{self.name}: {self.height}cm, {self.age} days old"

def plant_factory() -> list[Plant]:
	"""
    Creates multiple plants returns them as a list.
    """
	plants = [
		("Rose", 25, 30),
		("Oak", 200, 365),
		("Cactus", 5, 90),
		("Sunflower", 80, 450),
		("Fern", 15, 120)
	]
	total_plants = []
	for name, height, age in plants:
		new_plant = Plant(name, height, age)
		print(f"Created: {new_plant}")
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