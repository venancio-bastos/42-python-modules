import sys

def parse_inventory(args: list[str]) -> dict[str, int]:
    """
    Parses command line arguments in the format 'item:quantity'
    and builds the initial inventory dictionary.
    """
    inventory: dict[str, int] = {}
    
    for arg in args:
        if ":" in arg:
            parts = arg.split(":")
            if len(parts) == 2 and parts[1].isdigit():
                item_name = parts[0]
                quantity = int(parts[1])
                inventory[item_name] = quantity
                
    return inventory


def analyze_inventory(inventory: dict[str, int]) -> None:
    """
    Performs analytics on the inventory dictionary, demonstrating various
    dict methods like .items(), .keys(), and .values() [cite: 298-299].
    """
    print("=== Inventory System Analysis ===")
    
    if not inventory:
        print("Inventory is empty! Provide items like 'sword:1 potion:5'")
        return

    unique_items = len(inventory)
    
    total_items = 0
    for qty in inventory.values():
        total_items += qty

    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {unique_items}")
    
    print("\n=== Current Inventory ===")
    for item, qty in inventory.items():
        percentage = (qty / total_items) * 100
        word = "unit" if qty == 1 else "units"
        print(f"{item}: {qty} {word} ({percentage:.1f}%)")

    most_abundant_item = ""
    most_qty = -1
    least_abundant_item = ""
    least_qty = float('inf')

    for item, qty in inventory.items():
        if qty > most_qty:
            most_qty = qty
            most_abundant_item = item
        if qty < least_qty:
            least_qty = qty
            least_abundant_item = item

    print("\n=== Inventory Statistics ===")
    print(f"Most abundant: {most_abundant_item} ({most_qty} units)")
    print(f"Least abundant: {least_abundant_item} ({least_qty} units)")

    categories: dict[str, dict[str, int]] = {
        "Moderate": {},
        "Scarce": {}
    }
    
    restock_needed: list[str] = []

    for item, qty in inventory.items():
        if qty >= 5:
            categories["Moderate"][item] = qty
        else:
            categories["Scarce"][item] = qty
            if qty < 2:
                restock_needed.append(item)

    print("\n=== Item Categories ===")
    print(f"Moderate: {categories['Moderate']}")
    print(f"Scarce: {categories['Scarce']}")
    
    print("\n=== Management Suggestions ===")
    print(f"Restock needed: {restock_needed}")

    print("\n=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {list(inventory.keys())}")
    print(f"Dictionary values: {list(inventory.values())}")
    
    check_item = "sword"
    has_sword = inventory.get(check_item) is not None
    print(f"Sample lookup: '{check_item}' in inventory: {has_sword}")
    
    inventory.update({"magic_bean": 10})


def main() -> None:
    """Main execution function."""
    inventory = parse_inventory(sys.argv[1:])
    analyze_inventory(inventory)


if __name__ == "__main__":
    main()