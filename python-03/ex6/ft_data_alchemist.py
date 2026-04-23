import random


def main() -> None:
    print("=== Game Data Alchemist ===")

    players = [
        'Alice',
        'bob',
        'Charlie',
        'dylan',
        'Emma',
        'Gregory',
        'john',
        'kevin',
        'Liam'
    ]
    print(f"\nInitial list of players: {players}")

    cap_all = [p.capitalize() for p in players]
    print(f"New list with all names capitalized: {cap_all}")

    only_cap = [p for p in players if p[0].isupper()]
    print(f"New list of capitalized names only: {only_cap}")

    scores = {p: random.randint(0, 1000) for p in cap_all}
    print(f"\nScore dict: {scores}")

    avg = sum(scores.values()) / len(scores)
    print(f"Score average is {round(avg, 2)}")

    high = {k: v for k, v in scores.items() if v > avg}
    print(f"High scores: {high}")


if __name__ == "__main__":
    main()
