def main() -> None:
    filename = "../new_discovery.txt"

    print("=== CYBER ARCHIVES PRESERVATION SYSTEM ===")
    print(f"Initializing new storage unit: {filename}...")
    print("Storage unit created successfully.\n")

    vault = open(filename, 'w')

    print("Inscribing preservation data...")

    entry1 = "[ENTRY 001] New quantum algorithm discovered"
    entry2 = "[ENTRY 002] Efficiency increased by 347%"
    entry3 = "[ENTRY 003] Archived by Data Archivist trainee"

    print(entry1)
    print(entry2)
    print(entry3)

    vault.write(entry1 + "\n")
    vault.write(entry2 + "\n")
    vault.write(entry3 + "\n")

    vault.close()

    print("\nData inscription complete. Storage unit sealed.")
    print(f"Archive '{filename}' ready for long-term preservation.")


if __name__ == "__main__":
    main()
