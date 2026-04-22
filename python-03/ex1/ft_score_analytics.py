import sys


def main() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")

    if len(sys.argv) < 2:
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return

    scores = []
    for i in sys.argv[1:]:
        if sys.argv[i] is not int():
            print(f"Invalid parameter: '{sys.argv[i]}'")
        else:
            scores.append(sys.argv[i])
    if len(scores == 0):
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return
    print(f"Scores processed: {scores}")



if __name__ == "__main__":
    main()