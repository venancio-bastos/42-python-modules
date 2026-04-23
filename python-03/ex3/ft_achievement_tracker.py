import random


def gen_player_achievements() -> set[str]:
    pool = [
        'Crafting Genius', 'World Savior', 'Master Explorer',
        'Collector Supreme', 'Untouchable', 'Boss Slayer', 'Strategist',
        'Speed Runner', 'Survivor',
        'Treasure Hunter', 'First Steps', 'Sharp Mind',
        'Hidden Path Finder', 'Unstoppable'
    ]
    num_achievements = random.randint(5, 9)
    return set(random.sample(pool, num_achievements))


def main() -> None:
    print("=== Achievement Tracker System ===")

    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()

    print(f"\nPlayer Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")

    all_distinct = alice.union(bob).union(charlie).union(dylan) sword:1 potion:5 shield:2 armor:3 helmet:1 sword:2 hello key:value
    print(f"\nAll distinct achievements: {all_distinct}")

    common = alice.intersection(bob).intersection(charlie).intersection(dylan)
    print(f"\nCommon achievements: {common}")

    print(
        "\nOnly Alice has: "
        f"{alice.difference(bob.union(charlie).union(dylan))}"
    )
    print(f"Only Bob has: {bob.difference(alice.union(charlie).union(dylan))}")
    print(
        "Only Charlie has: "
        f"{charlie.difference(alice.union(bob).union(dylan))}"
    )
    print(
        f"Only Dylan has: {dylan.difference(alice.union(bob).union(charlie))}"
    )

    print(f"\nAlice is missing: {all_distinct.difference(alice)}")
    print(f"Bob is missing: {all_distinct.difference(bob)}")
    print(f"Charlie is missing: {all_distinct.difference(charlie)}")
    print(f"Dylan is missing: {all_distinct.difference(dylan)}")


if __name__ == "__main__":
    main()
