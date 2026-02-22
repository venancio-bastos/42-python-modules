class GardenError(Exception):
    """Base exception class for all garden-related problems[cite: 189]."""
    pass


class PlantError(GardenError):
    """Exception raised for problems specific to plants[cite: 190]."""
    pass


class WaterError(GardenError):
    """Exception raised for problems related to the watering system[cite: 191]."""
    pass


def simulate_plant_problem() -> None:
    """Simulates a situation that raises a PlantError ."""
    raise PlantError("The tomato plant is wilting!")


def simulate_water_problem() -> None:
    """Simulates a situation that raises a WaterError ."""
    raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    """
    Demonstrates raising and catching custom garden exceptions,
    including catching all errors using the base class GardenError [cite: 199-202].
    """
    print("=== Custom Garden Errors Demo ===\n")
    
    try:
        print("Testing PlantError...")
        simulate_plant_problem()
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")
        
    try:
        print("Testing WaterError...")
        simulate_water_problem()
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")
        
    print("Testing catching all garden errors...")
    try:
        simulate_plant_problem()
    except GardenError as e:
        print(f"Caught a garden error: {e}")
        
    try:
        simulate_water_problem()
    except GardenError as e:
        print(f"Caught a garden error: {e}")
        
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()