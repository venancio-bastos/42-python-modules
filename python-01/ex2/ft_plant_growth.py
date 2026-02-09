#!/usr/bin/env python3

class Plant:
	"""
	Acts as a blueprint for Plant objects.
	"""
	def __init__(self, name: str, height: float, days_old: int) -> None:
		"""
        Constructs a Plant object.
        """
		self.name = name
		self.height = height
		self.days_old = days_old
	def grow(self) -> None:
		"""
        Increases the plant's height by 1 unit.
        """
		self.height +=1
	def age(self) -> None:
		"""
		Increases the plant's lifetime by 1 day.
		"""
		self.days_old += 1
	def get_info(self) -> str:
		"""
		Returns a readable string representation of the plant.
		"""
		return f"{self.name}: {self.height}cm, {self.days_old} days old"

def main() -> None:
	"""
    Simulates plant's growth.
    """
	garden = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120)
    ]
	init_height = [plant.height for plant in garden]
	print("=== Day 1 ===")
	for plant in garden:
		print(plant.get_info())
	for day in range(1, 7):
		for plant in garden:
			plant.grow()
			plant.age()
	print("=== Day 7 ===")
	i = 0
	for plant in garden:
		growth = plant.height - init_height[i]
		print(plant.get_info())
		print(f"Growth this week: +{growth}cm")
		i += 1

if __name__ == "__main__":
	main()