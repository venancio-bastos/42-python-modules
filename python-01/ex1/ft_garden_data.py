class Plant:
	"""
	Plant object.
	"""
	def __init__(self, name: str, height: float, age: int) -> None:
		"""
        Plant object constructs.
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
    Displays plant's information.
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