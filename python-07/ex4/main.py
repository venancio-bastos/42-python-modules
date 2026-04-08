from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    print("=== DataDeck Tournament Platform ===")
    print("Registering Tournament Cards...")

    dragon = TournamentCard(
        "dragon_001", "Fire Dragon", 5, "Legendary", 7, 5
    )
    dragon.base_rating = 1200
    
    wizard = TournamentCard(
        "wizard_001", "Ice Wizard", 4, "Epic", 4, 3
    )
    wizard.base_rating = 1150

    platform = TournamentPlatform()
    platform.register_card(dragon)
    platform.register_card(wizard)

    print("Fire Dragon (ID: dragon_001):")
    print("Interfaces: [Card, Combatable, Rankable]")
    print(f"Rating: {dragon.calculate_rating()}")
    print("Record: 0-0")

    print("Ice Wizard (ID: wizard_001):")
    print("Interfaces: [Card, Combatable, Rankable]")
    print(f"Rating: {wizard.calculate_rating()}")
    print("Record: 0-0")

    print("\nCreating tournament match...")
    match_res = platform.create_match("dragon_001", "wizard_001")
    
    # Formatted exactly to match the PDF requirements
    print(f"Match result: {{'winner': '{match_res['winner']}', "
          f"'loser': '{match_res['loser']}',")
    print(f"'winner_rating': {match_res['winner_rating']}, "
          f"'loser_rating': {match_res['loser_rating']}}}")

    print("\nTournament Leaderboard:")
    board = platform.get_leaderboard()
    print(
        f"1. {board[0]['name']}\n"
        f"Rating: {board[0]['rating']} ({board[0]['record']})"
    )
    print(
        f"2. {board[1]['name']} Rating: {board[1]['rating']} "
        f"({board[1]['record']})"
    )

    print("\nPlatform Report:")
    print(platform.generate_tournament_report())

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
