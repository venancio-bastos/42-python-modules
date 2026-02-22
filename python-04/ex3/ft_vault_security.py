def main() -> None:
    """
    Implements secure file operations using context managers (the 'with' statement).
    Demonstrates automatic resource cleanup for both extraction and preservation protocols [cite: 243-244, 253-254].
    """
    print("=== CYBER ARCHIVES VAULT SECURITY SYSTEM ===")
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols.\n")

    with open("classified_data.txt", "w") as setup_vault:
        setup_vault.write("[CLASSIFIED] Quantum encryption keys recovered\n[CLASSIFIED] Archive integrity: 100%")

    print("SECURE EXTRACTION:")
    
    with open("classified_data.txt", "r") as extraction_vault:
        extracted_data = extraction_vault.read()
        print(extracted_data)

    print("\nSECURE PRESERVATION:")
    
    with open("new_security_protocols.txt", "w") as preservation_vault:
        preservation_data = "[CLASSIFIED] New security protocols archived"
        preservation_vault.write(preservation_data + "\n")
        print(preservation_data)

    print("\nVault automatically sealed upon completion.")
    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    main()