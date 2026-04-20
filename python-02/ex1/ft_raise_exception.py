def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    
    if temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    if temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
        
    return temp


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")
    
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

    test_hot = "100"
    print(f"\nInput data is '{test_hot}'")
    try:
        temp = input_temperature(test_hot)
        print(f"Temperature is now {temp}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")

    test_cold = "-50"
    print(f"\nInput data is '{test_cold}'")
    try:
        temp = input_temperature(test_cold)
        print(f"Temperature is now {temp}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")

    print("\nAll tests completed program didn't crash!")


if __name__ == "__main__":
    test_temperature()