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

def main() -> None:
	"""
    Displays plant's their information.
    """
	plant = Plant("Rosa", 25, 30)
	print("=== Welcome to My Garden ===")
	print(f"Plant: {plant.name}")
	print(f"Height: {plant.height}cm")
	print(f"Age: {plant.age} days")
	print(f"\n=== End of Program ===")

if __name__ == "__main__":
	main()