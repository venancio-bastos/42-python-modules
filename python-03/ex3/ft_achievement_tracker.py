def print_player_stats(alice: set[str], bob: set[str], charlie: set[str]) -> None:
    """
    Demonstrates set operations (union, intersection, difference) 
    to analyze game achievements across multiple players.
    """
    print("=== Achievement Analytics ===")
    
    all_achievements = alice.union(bob).union(charlie)
    print(f"All unique achievements: {all_achievements}")
    print(f"Total unique achievements: {len(all_achievements)}")
    
    common_all = alice.intersection(bob).intersection(charlie)
    print(f"Common to all players: {common_all}")
    
    alice_only = alice.difference(bob.union(charlie))
    bob_only = bob.difference(alice.union(charlie))
    charlie_only = charlie.difference(alice.union(bob))
    
    rare_achievements = alice_only.union(bob_only).union(charlie_only)
    print(f"Rare achievements (1 player): {rare_achievements}")
    
    alice_bob_common = alice.intersection(bob)
    print(f"Alice vs Bob common: {alice_bob_common}")
    
    alice_unique_vs_bob = alice.difference(bob)
    print(f"Alice unique: {alice_unique_vs_bob}")
    
    bob_unique_vs_alice = bob.difference(alice)
    print(f"Bob unique: {bob_unique_vs_alice}")


def main() -> None:
    """
    Initializes player achievement sets and runs the analytics system.
    Demonstrates how sets naturally handle unique collections [cite: 262-263, 276-279].
    """
    print("=== Achievement Tracker System ===")
    
    alice_achievements: set[str] = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob_achievements: set[str] = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie_achievements: set[str] = {'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon', 'perfectionist'}
    
    print(f"Player alice achievements: {alice_achievements}")
    print(f"Player bob achievements: {bob_achievements}")
    print(f"Player charlie achievements: {charlie_achievements}\n")
    
    print_player_stats(alice_achievements, bob_achievements, charlie_achievements)


if __name__ == "__main__":
    main()