from ex2.EliteCard import EliteCard


def main() -> None:
    print("=== DataDeck Ability System ===")
    print("EliteCard capabilities:")
    
    print(f"Card: {['play', 'get_card_info', 'is_playable']}")
    print(f"Combatable: {['attack', 'defend', 'get_combat_stats']}")
    print(f"Magical: {['cast_spell', 'channel_mana', 'get_magic_stats']}")

    print("\nPlaying Arcane Warrior (Elite Card):")
    warrior = EliteCard("Arcane Warrior", 6, "Epic", 5, 10, 8)

    print("Combat phase:")
    print(f"Attack result: {warrior.attack('Enemy')}")
    print(f"Defense result: {warrior.defend(5)}")

    print("Magic phase:")
    print(
        f"Spell cast: "
        f"{warrior.cast_spell('Fireball', ['Enemy1', 'Enemy2'])}"
    )
    print(f"Mana channel: {warrior.channel_mana(3)}")

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
