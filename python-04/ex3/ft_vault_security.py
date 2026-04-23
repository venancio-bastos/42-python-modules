import typing


def secure_archive(filename: str, action: typing.Union[int, str] = 'read', content: str = "") -> tuple[bool, str]:
    """
    Provides safe access to any file for reading or writing using 'with'.
    """
    try:
        if action == 'read' or action == 0:
            with open(filename, 'r') as f:
                file_content = f.read()
                return (True, file_content)
                
        elif action == 'write' or action == 1:
            with open(filename, 'w') as f:
                f.write(content)
                return (True, "Content successfully written to file")
                
        else:
            return (False, "Invalid action specified")
            
    except OSError as e:
        return (False, str(e))


def main() -> None:
    print("=== Cyber Archives Security ===")
    
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file", 'read'))
    
    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd", 'read'))
    
    print("Using 'secure_archive' to read from a regular file:")
    print(secure_archive("ancient_fragment.txt", 'read'))
    
    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new_fragment.txt", 'write', "Some secret content"))


if __name__ == "__main__":
    main()