from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


def main() -> None:
    print("=== DataDeck Deck Builder ===")
    print("Building deck with different card types...")

    deck = Deck()
    deck.add_card(SpellCard("Lightning Bolt", 3, "Common", "damage"))
    deck.add_card(
        ArtifactCard(
            "Mana Crystal", 2, "Rare", 10, "Permanent: +1 mana per turn"
        )
    )
    deck.add_card(CreatureCard("Fire Dragon", 5, "Legendary", 7, 5))

    print(f"Deck stats: {deck.get_deck_stats()}")
    print("\nDrawing and playing cards:")

    c1 = deck.draw_card()
    print(f"Drew: {c1.name} (Spell)")
    print(f"Play result: {c1.play({})}")

    c2 = deck.draw_card()
    print(f"Drew: {c2.name} (Artifact)")
    print(f"Play result: {c2.play({})}")

    c3 = deck.draw_card()
    print(f"Drew: {c3.name} (Creature)")
    print(f"Play result: {c3.play({})}")

    print(
        "\nPolymorphism in action: Same interface, different card behaviors!"
    )


if __name__ == "__main__":
    main()
