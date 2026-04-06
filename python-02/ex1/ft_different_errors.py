def garden_operations(error_to_trigger: str) -> None:
    if error_to_trigger == "value":
        int("abc")
    elif error_to_trigger == "zero":
        print(10 / 0)
    elif error_to_trigger == "file":
        open("missing.txt", "r")
    elif error_to_trigger == "key":
        test = {"plant": "Rose"}
        print(test["missing_plant"])
    elif error_to_trigger == "multiple":
        int("invalid")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")

    try:
        print("\nTesting ValueError...")
        garden_operations("value")
    except ValueError as e:
        print("Caught ValueError: invalid literal for int()")

    try:
        print("\nTesting ZeroDivisionError...")
        garden_operations("zero")
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")

    try:
        print("\nTesting FileNotFoundError...")
        garden_operations("file")
    except FileNotFoundError as e:
        print("Caught FileNotFoundError: No such file 'missing.txt'")

    try:
        print("\nTesting KeyError...")
        garden_operations("key")
    except KeyError as e:
        print(f"Caught KeyError: 'missing\\_plant'")

    try:
        print("\nTesting multiple errors together...")
        garden_operations("multiple")
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!")

    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
