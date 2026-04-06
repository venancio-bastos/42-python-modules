def main() -> None:
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
