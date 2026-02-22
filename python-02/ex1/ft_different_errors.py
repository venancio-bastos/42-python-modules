def garden_operations(error_to_trigger: str) -> None:
    """
    Executes specific garden operations that are designed to fail,
    demonstrating different built-in Python exceptions.
    """
    if error_to_trigger == "value":
        int("abc")
    elif error_to_trigger == "zero":
        print(10 / 0)
    elif error_to_trigger == "file":
        open("test.txt", "r")
    elif error_to_trigger == "key":
        test = {"plant": "Rose"}
        print(test["missing_plant"])
    elif error_to_trigger == "multiple":
        int("invalid")


def test_error_types() -> None:
    """
    Calls the garden operations, catches each specific error, 
    explains what went wrong, and keeps the program running [cite: 156-159].
    """
    print("=== Garden Error Types Demo ===")
    
    try:
        print("Testing ValueError...")
        garden_operations("value")
    except ValueError as e:
        print(f"Caught ValueError: {e}")
    
    try:
        print("Testing ZeroDivisionError...")
        garden_operations("zero")
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")

    try:
        print("Testing FileNotFoundError...")
        garden_operations("file")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")

    try:
        print("Testing KeyError...")
        garden_operations("key")
    except KeyError as e:
        print(f"Caught KeyError: {e}")

    try:
        print("Testing multiple errors together...")
        garden_operations("multiple")
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!")
        
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()