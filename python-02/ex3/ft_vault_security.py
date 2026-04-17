from typing import Union, Tuple


def secure_archive(
    filename: str, 
    action: Union[str, int] = "read", 
    content: str = ""
) -> Tuple[bool, str]:
    if action == "read" or action == 0:
        try:
            with open(filename, 'r') as file:
                data = file.read()
            return True, data
        except OSError as e:
            return False, str(e)
            
    elif action == "write" or action == 1:
        try:
            with open(filename, 'w') as file:
                file.write(content)
            return True, "Content successfully written to file"
        except OSError as e:
            return False, str(e)
            
    return False, "Invalid action specified."


def main() -> None:
    print("=== Cyber Archives Security ===")
    
    print("Using 'secure_archive' to read from a nonexistent file:")
    res_no_file = secure_archive("/not/existing/file", "read")
    print(res_no_file)
    
    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    res_no_perm = secure_archive("/etc/master.passwd", "read")
    print(res_no_perm)
    
    sample_data = (
        "[FRAGMENT 001] Digital preservation protocols established 2087\n"
        "[FRAGMENT 002] Knowledge must survive the entropy wars\n"
        "[FRAGMENT 003] Every byte saved is a victory against oblivion\n"
    )
    secure_archive("test_fragment.txt", "write", sample_data)
    
    print("\nUsing 'secure_archive' to read from a regular file:")
    res_read = secure_archive("test_fragment.txt", "read")
    print(res_read)
    
    print("\nUsing 'secure_archive' to write previous content to a new file:")
    res_write = secure_archive("new_fragment.txt", "write", res_read[1])
    print(res_write)


if __name__ == "__main__":
    main()
