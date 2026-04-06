import alchemy.grimoire.validator
import alchemy.grimoire.spellbook


def main() -> None:
    print("=== Circular Curse Breaking ===")

    print("\nTesting ingredient validation:")

    res1 = alchemy.grimoire.validator.validate_ingredients("fire air")
    print(f"validate_ingredients(\"fire air\"): {res1}")

    res2 = alchemy.grimoire.validator.validate_ingredients("dragon scales")
    print(f"validate_ingredients(\"dragon scales\"): {res2}")

    print("\nTesting spell recording with validation:")

    res3 = alchemy.grimoire.spellbook.record_spell("Fireball", "fire air")
    print(f"record_spell(\"Fireball\", \"fire air\"): {res3}")

    res4 = alchemy.grimoire.spellbook.record_spell("Dark Magic", "shadow")
    print(f"record_spell(\"Dark Magic\", \"shadow\"): {res4}")

    print("\nTesting late import technique:")

    res5 = alchemy.grimoire.spellbook.record_spell("Lightning", "air")
    print(f"record_spell(\"Lightning\", \"air\"): {res5}")

    print("\nCircular dependency curse avoided using late imports!")
    print("All spells processed safely!")


if __name__ == "__main__":
    main()
