def crisis_handler(filename: str, access_type: str) -> None:
    print(f"{access_type}: Attempting access to '{filename}'...")

    try:
        with open(filename, 'r') as vault:
            content = vault.read().strip()
            print(f"SUCCESS: Archive recovered {content}")
            print("STATUS: Normal operations resumed\n")

    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")

    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained\n")

    except Exception as e:
        print(f"RESPONSE: Unexpected system anomaly: {e}")
        print("STATUS: System stabilized\n")


def main() -> None:
    print("=== CYBER ARCHIVES CRISIS RESPONSE SYSTEM ===\n")

    crisis_handler("lost_archive.txt", "CRISIS ALERT")
    crisis_handler("classified_vault.txt", "CRISIS ALERT")
    crisis_handler("standard_archive.txt", "ROUTINE ACCESS")

    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()

