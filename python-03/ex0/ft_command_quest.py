import sys

def main() -> None:
    """
    Acts as a simple command interpreter.
    Reads and displays command-line arguments passed by the user,
    handling both empty and populated argument lists [cite: 142, 145-148].
    """
    print("=== Command Quest ===")

    if len(sys.argv) == 1:
        print("No arguments provided!")
        print(f"Program name: {sys.argv[0]}")
        print(f"Total arguments: {len(sys.argv)}")
        return

    print(f"Program name: {sys.argv[0]}")
    print(f"Arguments received: {len(sys.argv) - 1}")
    
    i = 1
    for arg in sys.argv[1:]:
        print(f"Argument {i}: {arg}")
        i += 1
        
    print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    main()