def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===")

    test_valid = "25"
    print(f"\nInput data is '{test_valid}'")
    try:
        temp = input_temperature(test_valid)
        print(f"Temperature is now {temp}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")


    test_invalid = "abc"
    print(f"\nInput data is '{test_invalid}'")
    try:
        temp = input_temperature(test_invalid)
        print(f"Temperature is now {temp}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")

    print("\nAll tests completed program didn't crash!")


if __name__ == "__main__":
    test_temperature()
