def main() -> None:
    """
    Acts as a digital archaeology tool to recover data from an ancient storage vault.
    Demonstrates fundamental file reading and manual resource management using close() [cite: 135, 142-143].
    """
    filename = "../ancient_fragment.txt"
    print("=== CYBER ARCHIVES ===")
    print("=== DATA RECOVERY SYSTEM ===")
    print(f"Accessing Storage Vault: {filename}")
    try:
        vault = open(filename, 'r')
        print("Connection established...\n")
        print("RECOVERED DATA:")
        content = vault.read()
        print(content, end="")
        vault.close()
        print("\nData recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")

if __name__ == "__main__":
    main()