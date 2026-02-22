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

def main() -> None:
	"""
    Displays plant's information.
    """
	plant = Plant("Rosa", 25, 30)
	print("=== Welcome to My Garden ===")
	print(f"Plant: {plant.name}")
	print(f"Height: {plant.height}cm")
	print(f"Age: {plant.age} days")
	print(f"\n=== End of Program ===")

if __name__ == "__main__":
	main()