
class GardenManager:
    """
    Manages a collection of plants and provides garden statistics.
    """
    total_gardens = 0

    def __init__(self, owner_name: str = "Unknown") -> None:
		"""
		Initializes the garden manager for a specific owner.
		"""
        self.plants = []
        self.owner_name = owner_name
        self.stats = self.GardenStats()
        GardenManager.total_gardens += 1

    @staticmethod
    def validate_height(height: float) -> bool:
		"""
        Utility function that validates if a given height is acceptable 
		(greater than zero).
        """
        return height > 0

    @classmethod
    def create_garden_network(cls, quantity: int) -> list:
		"""
        Creates a network of multiple gardens.
        """
        names = ["Alice", "Bob"]
        network = []
        for i in range(quantity):
            name = names[i] if i < len(names) else f"Garden {i+1}"
            new_garden = cls(name)
            network.append(new_garden)
        return network

    def add_plant(self, plant) -> None:
		"""
		Adds a plant to the garden if its height is valid.
		"""
        if self.validate_height(plant.height):
            self.plants.append(plant)
            print(f"Added {plant.name} to {self.owner_name}'s garden")
        else:
            print(f"Cannot add {plant.name}: Invalid height.")

    def get_report(self) -> None:
		"""
		Prints a comprehensive report of the garden's current state.
		"""
        print(f"\n=== {self.owner_name}'s Garden Report ===")
        print("Plants in garden:")
        for p in self.plants:
            print(p)
        
        count = len(self.plants)
        total_growth = sum(p.growth_amount for p in self.plants)
        print(f"\nPlants added: {count}, Total growth: {total_growth}cm")

        n_regular = sum(1 for p in self.plants if type(p) == Plant)
        n_flowering = sum(1 for p in self.plants if type(p) == FloweringPlant)
        n_prize = sum(1 for p in self.plants if type(p) == PrizeFlower)
        
        print(f"Plant types: {n_regular} regular, {n_flowering} flowering, {n_prize} prize flowers")

	class GardenStats:
        """
        Helper class to calculate statistics.
        """
        def calculate_score(self, plants: list) -> int:
			"""
			Calculates the total score of a garden based on heights and prizes.
			"""
            score = 0
            for p in plants:
                score += p.height
                if hasattr(p, 'prize'):
                    score += p.prize
            return int(score)

class Plant:
	"""
	Base class representing a generic plant in the garden.
	"""
    def __init__(self, name: str, height: float) -> None:
		"""
        Plant object constructs.
        """
        self.name = name
        self.height = height
        self.growth_amount = 0

    def __str__(self) -> str:
		"""
        Returns the string representation of the plant.
        """
        return f"- {self.name}: {self.height}cm"

    def grow(self) -> str:
		"""
		Increases the plant's height and tracks growth.
		"""
        self.height += 1
        self.growth_amount += 1
        return f"{self.name} grew 1cm"

class FloweringPlant(Plant):
	"""
	Class representing a plant that produces flowers.
	"""
    def __init__(self, name: str, height: float, color: str) -> None:
		"""
        FloweringPlant object constructs.
        """
        super().__init__(name, height)
        self.color = color
    
    def __str__(self) -> str:
		"""
        Returns the string representation of the flowering plant.
        """
        return super().__str__() + f", {self.color} flowers (blooming)"

class PrizeFlower(FloweringPlant):
	"""
	Class representing a premium flowering plant with prize points.
	"""
    def __init__(self, name: str, height: float, color: str, prize: int) -> None:
		"""
        PrizeFlower object constructs.
        """
        super().__init__(name, height, color)
        self.prize = prize

    def __str__(self) -> str:
		"""
		Returns the string representation of the prize flower.
		"""
        return super().__str__() + f", Prize points: {self.prize}"

def main() -> None:
	"""
	Main function to demonstrate the garden management system.
	"""
    print("=== Garden Management System Demo ===\n")

    gardens = GardenManager.create_garden_network(2)
    alice_garden = gardens[0]
    
    p1 = Plant("Oak Tree", 100)
    p2 = FloweringPlant("Rose", 25, "red")
    p3 = PrizeFlower("Sunflower", 50, "yellow", 10)

    alice_garden.add_plant(p1)
    alice_garden.add_plant(p2)
    alice_garden.add_plant(p3)

    print("\nAlice is helping all plants grow...")
    for p in alice_garden.plants:
        print(p.grow())

    alice_garden.get_report()

    print(f"\nHeight validation test: {GardenManager.validate_height(10)}")
    
    scores_str = []
    for g in gardens:
        score = g.stats.calculate_score(g.plants)
        scores_str.append(f"{g.owner_name}: {score}")
    
    print(f"Garden scores - {', '.join(scores_str)}")
    print(f"Total gardens managed: {GardenManager.total_gardens}")

if __name__ == "__main__":
    main()