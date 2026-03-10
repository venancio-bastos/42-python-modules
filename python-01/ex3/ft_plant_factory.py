class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


def plant_factory() -> list[Plant]:
    plants = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120)
    ]
    total_plants = []
    for name, height, age in plants:
        new_plant = Plant(name, height, age)
        print(
            f"Created: {new_plant.name} ({new_plant.height}cm, "
            f"{new_plant.age} days)"
        )
        total_plants.append(new_plant)
    return total_plants


def main() -> None:
    print("=== Plant Factory Output ===")
    plants = plant_factory()
    print(f"\nTotal plants created: {len(plants)}")


if __name__ == "__main__":
    main()
