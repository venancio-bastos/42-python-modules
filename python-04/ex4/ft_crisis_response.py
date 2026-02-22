def crisis_handler(filename: str, access_type: str) -> None:
    """
    Handles access attempts to storage vaults, managing potential crisis 
    scenarios like missing files or permission denials using failsafe protocols [cite: 290-291, 295].
    """
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
    """
    Executes the ultimate trial for Data Archivists, testing response protocols
    against non-existent archives, restricted vaults, and standard data [cite: 281-282, 296].
    """
    print("=== CYBER ARCHIVES CRISIS RESPONSE SYSTEM ===\n")
    
    crisis_handler("lost_archive.txt", "CRISIS ALERT")
    crisis_handler("classified_vault.txt", "CRISIS ALERT")
    crisis_handler("standard_archive.txt", "ROUTINE ACCESS")
    
    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()