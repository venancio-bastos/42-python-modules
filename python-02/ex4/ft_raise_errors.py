def check_plant_health(plant_name: str | None, water_level: int, sunlight_hours: int) -> None:
    """
    Checks if plant parameters are within acceptable ranges.
    Raises ValueError with specific messages if validation fails.
    """
    if not plant_name:
        raise ValueError("Plant name cannot be empty!")

    if water_level < 1 or water_level > 10:
        raise ValueError(f"Water level {water_level} is out of bounds (must be 1-10)")

    if sunlight_hours < 2 or sunlight_hours > 12:
        raise ValueError(f"Sunlight hours {sunlight_hours} is out of bounds (must be 2-12)")
        
    print(f"Plant '{plant_name}' is healthy!\n")


def test_plant_checks() -> None:
    """
    Demonstrates the plant health checker by passing valid and invalid data,
    catching and handling the resulting ValueErrors.
    """
    test = [
        ("tomato", 10, 3, "Testing good values..."),
        (None, 5, 5, "Testing empty plant name..."),
        ("tomato", 15, 3, "Testing bad water level..."),
        ("tomato", 10, 0, "Testing bad sunlight hours...")
    ]
    
    print("=== Garden Plant Health Checker ===\n")
    for name, water, sun, message in test:
        print(message)
        try:
            check_plant_health(name, water, sun)
        except ValueError as e:
            print(f"Error: {e}\n")
            
    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()