import sys


def main() -> None:
    print("=== Player Score Analytics ===")

    if len(sys.argv) < 2:
        print(
            "No scores provided. "
            "Usage: python3 ft_score_analytics.py <score1> <score2> ..."
        )
        return

    scores = []

    for arg in sys.argv[1:]:
        try:
            score = int(arg)
            scores.append(score)
        except ValueError:
            print(f"Invalid parameter: '{arg}'")

    if len(scores) == 0:
        print(
            "No scores provided. "
            "Usage: python3 ft_score_analytics.py <score1> <score2> ..."
        )
        return

    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")

    total_score = sum(scores)
    print(f"Total score: {total_score}")
    print(f"Average score: {total_score / len(scores)}")

    high_score = max(scores)
    print(f"High score: {high_score}")

    low_score = min(scores)
    print(f"Low score: {low_score}")
    print(f"Score range: {high_score - low_score}")


if __name__ == "__main__":
    main()
