import sys
import typing


def read_ancient_text(filename: str) -> None:
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")

    file: typing.IO | None = None
    try:
        file = open(filename, 'r')
        content: str = file.read()
        if content:
            print("---")
            print()
            print(content, end="\n\n---")
            if not content.endswith('\n'):
                print()
    except OSError as e:
        print(f"Error opening file '{filename}': {e}")
    finally:
        if file is not None:
            file.close()
            print(f"File '{filename}' closed.")


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    read_ancient_text(sys.argv[1])


if __name__ == "__main__":
    main()
