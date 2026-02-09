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

def main() -> None:
	"""
    Creates Plant's objects and displays their information.
    """
	garden = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120)
    ]
	print("=== Garden Plant Registry ===")
	for plant in garden:
		print(plant)

if __name__ == "__main__":
	main()