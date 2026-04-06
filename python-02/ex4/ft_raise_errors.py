def check_plant_health(
        plant_name: str | None,
        water_level: int,
        sunlight_hours: int
        ) -> None:
    if not plant_name:
        raise ValueError("Plant name cannot be empty!")

    if water_level < 1 or water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")

    if sunlight_hours < 2 or sunlight_hours > 12:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")

    print(f"Plant '{plant_name}' is healthy!")


def test_plant_checks() -> None:
    test = [
        ("tomato", 10, 3, "\nTesting good values..."),
        (None, 5, 5, "\nTesting empty plant name..."),
        ("tomato", 15, 3, "\nTesting bad water level..."),
        ("tomato", 10, 0, "\nTesting bad sunlight hours...")
    ]

    print("=== Garden Plant Health Checker ===")
    for name, water, sun, message in test:
        print(message)
        try:
            check_plant_health(name, water, sun)
        except ValueError as e:
            print(f"Error: {e}")
    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
