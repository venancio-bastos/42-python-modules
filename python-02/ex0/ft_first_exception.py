def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===")

    for value in ["25", "abc"]:
        print(f"\nInput data is '{value}'")
        try:
            temp = input_temperature(value)
            print(f"Temperature is now {temp}°C")
        except Exception as e:
            print(f"Caught input_temperature error: {e}")

    print("\nAll tests completed program didn't crash!")


if __name__ == "__main__":
    test_temperature()
