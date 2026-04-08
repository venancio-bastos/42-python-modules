def check_temperature(temp_str: str) -> int | None:
    try:
        temperature = int(temp_str)

        if temperature > 40:
<<<<<<< HEAD
            print(f"Error: {temperature}°C is too hot for plants (max 40°c)\n")
            return None
        elif temperature < 0:
            print(f"Error: {temperature}°C is too cold for plants (min 0°c)\n")
            return None
        return temperature
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number\n")
=======
            print(f"Error: {temperature}°C is too hot for plants (max 40°c)")
            return None
        elif temperature < 0:
            print(f"Error: {temperature}°C is too cold for plants (min 0°c)")
            return None
        return temperature
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
>>>>>>> f4b57bf491b4fb443877ba3362980ca5fb0706e5
        return None


def test_temperature_input() -> None:
    test_cases = ["25", "abc", "100", "-50"]

<<<<<<< HEAD
    print("=== Garden Temperature Checker ===\n")
=======
    print("=== Garden Temperature Checker ===")
>>>>>>> f4b57bf491b4fb443877ba3362980ca5fb0706e5
    for value in test_cases:
        print(f"Testing temperature: {value}")
        result = check_temperature(value)
        if result is not None:
<<<<<<< HEAD
            print(f"Temperature {value}°C is perfect for plants!\n")
=======
            print(f"Temperature {value}°C is perfect for plants!")
>>>>>>> f4b57bf491b4fb443877ba3362980ca5fb0706e5
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
