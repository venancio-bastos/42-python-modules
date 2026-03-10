class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def __str__(self) -> str:
        class_name = self.__class__.__name__
        return (
                f"\n{self.name} ({class_name}): "
                f"{self.height}cm, {self.age} days, "
            )


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> str:
        return f"{self.name} is blooming beautifully!"

    def __str__(self) -> str:
        default_message = super().__str__()
        return default_message + f"{self.color} color"


class Tree(Plant):
    def __init__(
            self,
            name: str,
            height: float,
            age: int,
            trunk_diameter: float
            ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> str:
        shade = self.height * 0.4
        return f"{self.name} provides {shade} square meters of shade"

    def __str__(self) -> str:
        default_message = super().__str__()
        return default_message + f"{self.trunk_diameter}cm diameter"


class Vegetable(Plant):
    def __init__(
            self,
            name: str,
            height: float,
            age: int,
            harvest_season: str,
            nutritional_value: str
            ) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show_benefits(self) -> str:
        return f"{self.name} is rich in {self.nutritional_value}"

    def __str__(self) -> str:
        default_message = super().__str__()
        return default_message + f"{self.harvest_season} harvest"


def main() -> None:
    flowers_data = [
        ("Rose", 25, 30, "red"),
        ("Sunflower", 80, 45, "yellow")
    ]
    trees_data = [
        ("Oak", 500, 1825, 50),
        ("Pine", 400, 1200, 35)
    ]

    vegetables_data = [
        ("Tomato", 80, 90, "summer", "vitamin C"),
        ("Lettuce", 30, 45, "spring", "fiber")
    ]

    print("=== Garden Plant Types ===")

    for name, height, age, color in flowers_data:
        plant = Flower(name, height, age, color)
        print(plant)
        print(plant.bloom())

    for name, height, age, trunk in trees_data:
        plant = Tree(name, height, age, trunk)
        print(plant)
        print(plant.produce_shade())

    for name, height, age, season, nut_val in vegetables_data:
        plant = Vegetable(name, height, age, season, nut_val)
        print(plant)
        print(plant.show_benefits())


if __name__ == "__main__":
    main()
