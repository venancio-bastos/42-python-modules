#!/usr/bin/env python3

class GardenError(Exception):
	pass

class PlantError(GardenError):
	pass

class WaterError(GardenError):
	pass

class GardenManager:
	def __init__(self):
		self.plants = []

	def add_plant(self, plant_name):
		try:
			if not plant_name:
				raise ValueError("Plant name cannot be empty!")
			self.plants.append(plant_name)
			print(f"Added {plant_name} successfully")
		except ValueError as e:
			print(f"Error adding plant: {e}")

	def water_plants(self):
		print("Opening watering system")
		try:
			for plant in self.plants:
				print(f"Watering {plant} - success")
		except Exception as e:
			print(f"Error during watering: {e}")
		finally:
			print("Closing watering system (cleanup)")

	def check_plant_health(self, plant_name, water_level, sunlight_hours):
		if water_level > 10:
			raise WaterError(f"Water level {water_level} is too high (max 10)")
		if sunlight_hours < 2:
			raise PlantError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
		print(f"{plant_name}: healthy (water: {water_level}, sun: {sunlight_hours})")

	def emergency_simulation(self):
		raise GardenError("Not enough water in tank")

def test_garden_management():
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
	print("\nGarden management system test complete!")

if __name__ == "__main__":
	test_garden_management()

