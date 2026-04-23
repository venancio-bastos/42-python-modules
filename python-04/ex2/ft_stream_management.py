import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python3 ft_stream_management.py <file>")
        return

    filename = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")

    file_in: typing.IO | None = None
    content: str = ""

    try:
        file_in = open(filename, 'r')
        content = file_in.read()
        print(content, end="")
        if not content.endswith('\n') and content != "":
            print()
    except OSError as e:
        print(f"[STDERR] Error opening file '{filename}': {e}", file=sys.stderr)
        return
    finally:
        if file_in is not None:
            file_in.close()
            print(f"File '{filename}' closed.")

    print("Transform data:")
    lines = content.splitlines()
    transformed_lines = [line + "#" for line in lines]
    new_content = '\n'.join(transformed_lines)
    if new_content:
        new_content += '\n'
        
    print(new_content, end="")

    print("Enter new file name (or empty): ", end="")
    sys.stdout.flush() 

    new_filename = sys.stdin.readline()
    
    if new_filename.endswith('\n'):
        new_filename = new_filename[:-1]

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
        print(f"[STDERR] Error opening file '{new_filename}': {e}", file=sys.stderr)
        print("Data not saved.")
    finally:
        if file_out is not None:
            file_out.close()


if __name__ == "__main__":
    main()