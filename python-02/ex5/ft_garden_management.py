class GardenError(Exception):
    """
	Base exception for general garden management errors.
	"""
    pass


class PlantError(GardenError):
    """
	Exception raised for plant-specific health issues.
	"""
    pass


class WaterError(GardenError):
    """
	Exception raised for water level issues.
	"""
    pass


class GardenManager:
    """
    Main system to manage garden operations, handling bad inputs gracefully
    and ensuring operations recover from errors.
    """
    
    def __init__(self) -> None: 
        """
		Initializes the garden manager with an empty list of plants.
		"""
        self.plants: list[str] = []

    def add_plant(self, plant_name: str) -> None:
        """
		Adds a plant to the garden, validating the input.
		"""
        try:
            if not plant_name:
                raise ValueError("Plant name cannot be empty!")
            self.plants.append(plant_name)
            print(f"Added {plant_name} successfully")
        except ValueError as e:
            print(f"Error adding plant: {e}")

    def water_plants(self) -> None:
        """
		Waters all plants and ensures the system is always closed.
		"""
        print("Opening watering system")
        try:
            for plant in self.plants:
                print(f"Watering {plant} - success")
        except Exception as e:
            print(f"Error during watering: {e}")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant_name: str, water_level: int, sunlight_hours: int) -> None:
        """
        Checks plant parameters and raises custom exceptions if they are out of bounds.
        """
        if water_level > 10:
            raise WaterError(f"Water level {water_level} is too high (max 10)")
        if sunlight_hours < 2:
            raise PlantError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
        print(f"{plant_name}: healthy (water: {water_level}, sun: {sunlight_hours})")

    def emergency_simulation(self) -> None:
        """
		Simulates a critical system error to test recovery.
		"""
        raise GardenError("Not enough water in tank")


def test_garden_management() -> None:
    """
    Integrates all error handling techniques, demonstrating normal operations
    and error recovery.
    """
    print("=== Garden Management System ===\n")
    
    manager = GardenManager()

    print("Adding plants to garden...")
    manager.add_plant("tomato")
    manager.add_plant("lettuce")
    manager.add_plant("")
    
    print("\nWatering plants...")
    manager.water_plants()
    
    print("\nChecking plant health...")
    try:
        manager.check_plant_health("tomato", 5, 8)
    except GardenError as e:
        print(f"Error: {e}")
        
    try:
        manager.check_plant_health("lettuce", 15, 8)
    except GardenError as e:
        print(f"Error checking lettuce: {e}")
    
    print("\nTesting error recovery...")
    try:
        manager.emergency_simulation()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...\n")
        
    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()