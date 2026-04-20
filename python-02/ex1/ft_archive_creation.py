import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python3 ft_archive_creation.py <file>")
        return

    filename = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")

    file_in: typing.IO | None = None
    content: str = ""

    try:
        file_in = open(filename, 'r')
        content = file_in.read()
        if content:
            print("---")
            print()
            print(content, end="")
            if not content.endswith('\n'):
                print()
    except OSError as e:
        print(f"Error opening file '{filename}': {e}")
        return
    finally:
        if file_in is not None:
            file_in.close()
            print(f"File '{filename}' closed.")

    print("\nTransform data:")
    lines = content.splitlines()
    transformed_lines = [line + "#" for line in lines]
    new_content = '\n'.join(transformed_lines)
    if new_content:
        print("---")
        print()
        new_content += '\n'

    print(f"{new_content}\n", end="")
    print("---")

    try:
        new_filename = input("Enter new file name (or empty): ")
    except EOFError:
        new_filename = ""
        print()

    if not new_filename:
        print("Not saving data.")
        return

    print(f"Saving data to '{new_filename}'")
    file_out: typing.IO | None = None

    try:
        file_out = open(new_filename, 'w')
        file_out.write(new_content)
        print(f"Data saved in file '{new_filename}'.")
    except OSError as e:
        print(f"Error opening file '{new_filename}': {e}")
    finally:
        if file_out is not None:
            file_out.close()


if __name__ == "__main__":
    main()
