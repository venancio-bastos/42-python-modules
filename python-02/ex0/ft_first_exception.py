def check_temperature(temp_str: str) -> int | None:
    try:
        temperature = int(temp_str)

        if temperature > 40:
            print(f"Error: {temperature}°C is too hot for plants (max 40°c)\n")
            return None
        elif temperature < 0:
            print(f"Error: {temperature}°C is too cold for plants (min 0°c)\n")
            return None
        return temperature
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number\n")
        return None


def test_temperature_input() -> None:
    test_cases = ["25", "abc", "100", "-50"]

    print("=== Garden Temperature Checker ===\n")
    for value in test_cases:
        print(f"Testing temperature: {value}")
        result = check_temperature(value)
        if result is not None:
            print(f"Temperature {value}°C is perfect for plants!\n")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
