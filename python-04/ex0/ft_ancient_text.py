import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python3 ft_ancient_text.py <file>")
        return

    filename = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")

    file: typing.IO | None = None
    try:
        file = open(filename, 'r')
        content = file.read()
        print("---")
        print("\n" + content, end="")

        if not content.endswith('\n') and content != "":
            print()
    except OSError as e:
        print(f"Error opening file '{filename}': {e}")
    finally:
        if file is not None:
            file.close()
            print("\n---")
            print(f"File '{filename}' closed.")


if __name__ == "__main__":
    main()
