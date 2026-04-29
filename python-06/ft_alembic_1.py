from alchemy import elements


def main() -> None:
    print("=== Alembic 1 ===")
    print("Using: 'from ... import ...' structure to access elements.py")
    print(f"Testing create_water: {elements.create_water()}")


if __name__ == "__main__":
    main()
