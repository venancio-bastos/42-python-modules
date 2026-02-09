#!/usr/bin/env python3

def check_plant_health(plant_name, water_level, sunlight_hours):
	if not plant_name:
		raise ValueError("Plant name cannot be empty!")
	if water_level > 10:
		raise ValueError(f"Water level {water_level} is too high (max 10)")
	if sunlight_hours < 2:
		raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
	print(f"Plant '{plant_name}' is healthy!\n")

def main():
	test = [
		("tomato", 10, 3, "Testing good values..."),
		(None, 1, 1, "Testing empty plant name..."),
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
	main()