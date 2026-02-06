#!/usr/bin/env python3

class GardenManager:
    """
    Manages a list of plants and provides statistics.
    """
    total_gardens = 0

    def __init__(self, owner_name: str = "Unknown") -> None:
        self.plants = []
        self.owner_name = owner_name
        self.stats = self.GardenStats()
        GardenManager.total_gardens += 1

    @staticmethod
    def validate_height(height: float) -> bool:
        return height > 0

    @classmethod
    def create_garden_network(cls, quantity: int) -> list:
        names = ["Alice", "Bob"]
        network = []
        for i in range(quantity):
            name = names[i] if i < len(names) else f"Garden {i+1}"
            new_garden = cls(name)
            network.append(new_garden)
        return network

    def add_plant(self, plant) -> None:
        if self.validate_height(plant.height):
            self.plants.append(plant)
            print(f"Added {plant.name} to {self.owner_name}'s garden")
        else:
            print(f"Cannot add {plant.name}: Invalid height.")

    def get_report(self) -> None:
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
            score = 0
            for p in plants:
                score += p.height
                if hasattr(p, 'prize'):
                    score += p.prize
            return int(score)


class Plant:
    def __init__(self, name: str, height: float) -> None:
        self.name = name
        self.height = height
        self.growth_amount = 0

    def __str__(self) -> str:
        return f"- {self.name}: {self.height}cm"

    def grow(self) -> str:
        self.height += 1
        self.growth_amount += 1
        return f"{self.name} grew 1cm"


class FloweringPlant(Plant):
    def __init__(self, name: str, height: float, color: str) -> None:
        super().__init__(name, height)
        self.color = color
    
    def __str__(self) -> str:
        return super().__str__() + f", {self.color} flowers (blooming)"


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: float, color: str, prize: int) -> None:
        super().__init__(name, height, color)
        self.prize = prize

    def __str__(self) -> str:
        return super().__str__() + f", Prize points: {self.prize}"


def main() -> None:
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