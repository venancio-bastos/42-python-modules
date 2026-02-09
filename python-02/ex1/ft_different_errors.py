#!/usr/bin/env python3

def garden_operations():
	print("=== Garden Error Types Demo ===")
	try:
		print("Testing ValueError...")
		int("abc")
	except ValueError as e:
		print(f"Caught ValueError: {e}")
	
	try:
		print("Testing ZeroDivisionError...")
		print(10 / 0)
	except ZeroDivisionError as e:
		print(f"Caught ZeroDivisionError: {e}")

	try:
		print("Testing FileNotFoundError...")
		open("test.txt", "r")
	except FileNotFoundError as e:
		print(f"Caught FileNotFoundError: {e}")

	try:
		print("Testing KeyError...")
		test = {"plant": "Rose"}
		print(test["missing_plant"])
	except KeyError as e:
		print(f"Caught KeyError: {e}")

	try:
		print("Testing multiple errors together...")
		int("invalid")
	except (ValueError, ZeroDivisionError) as e:
		print("Caught an error, but program continues!")
	pass

def test_error_types():
	garden_operations()
	print("All error types tested successfully!")

if __name__ == "__main__":
	test_error_types()