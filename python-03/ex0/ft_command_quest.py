import sys


def main() -> None:
    print("=== Command Quest ===")

    file_name = sys.argv[0].split('/')[-1]

    if len(sys.argv) == 1:
        print("No arguments provided!")
        print(f"Program name: {file_name}")
        print(f"Total arguments: {len(sys.argv)}")
        return

    print(f"Program name: {file_name}")
    print(f"Arguments received: {len(sys.argv) - 1}")

    i = 1
    for arg in sys.argv[1:]:
        print(f"Argument {i}: {arg}")
        i += 1
    print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    main()
