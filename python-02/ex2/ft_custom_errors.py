class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def simulate_plant_problem() -> None:
    raise PlantError("The tomato plant is wilting!")


def simulate_water_problem() -> None:
    raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===")

    try:
        print("\nTesting PlantError...")
        simulate_plant_problem()
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    try:
        print("\nTesting WaterError...")
        simulate_water_problem()
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("\nTesting catching all garden errors...")
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
