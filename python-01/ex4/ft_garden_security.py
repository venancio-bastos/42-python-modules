class SecurePlant:
	"""
	Plant objects.
	"""
	def __init__(self, name: str, height: float, age: int) -> None:
		"""
        Plant object constructs.
        """
		self._name = name
		self._height = height
		self._age = age

	def set_height(self, height: float) -> str:
			"""
			Set plant height.
			"""
			if height < 0:
				return (
					f"\nInvalid operation attempted: height {height}cm [REJECTED]\n"
					+ "Security: Negative height rejected"
				)
			self._height = height
			return f"Height updated: {height}cm [OK]"
	
	def get_height(self) -> int:
		"""
		Returns plant's height.
		"""
		return self._height

	def set_age(self, age: int) -> str:
		"""
		Set plant age.
		"""
		if age < 0:
			return (
				f"\nInvalid operation attempted: age {age} days [REJECTED]\n"
				+ "Security: Negative age rejected"
			) 
		self._age = age
		return f"Age updated: {age} days [OK]"

	def get_age(self) -> int:
		"""
		Returns plant's age.
		"""
		return self._age

def main() -> None:
	"""
	Display plant info.
	"""
	print("=== Garden Security System ===")
	plant = SecurePlant("Rose", 10, 20)
	print(f"Plant created: {plant._name}")
	print(plant.set_height(25))
	print(plant.set_age(30))
	print(plant.set_height(-5))
	print(f"\nCurrent plant: {plant._name} ({plant.get_height()}cm, {plant.get_age()} days)")

if __name__ == "__main__":
	main()