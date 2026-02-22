import sys

def main() -> None:
    """
    Analyzes player scores passed via command line.
    Uses a list to store valid scores, calculates statistics,
    and handles invalid non-numeric inputs gracefully [cite: 183, 188-190].
    """
    print("=== Player Score Analytics ===")

    if len(sys.argv) < 2:
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return

    scores: list[int] = []
    
    for arg in sys.argv[1:]:
        try:
            score = int(arg)
            scores.append(score)
        except ValueError:
    
            pass
    
    if not scores:
        print("No valid scores provided.")
        return

    total = sum(scores)
    count = len(scores)
    average = total / count
    highest = max(scores)
    lowest = min(scores)
    range_val = highest - lowest
    
    print(f"Scores processed: {scores}")
    print(f"Total players: {count}")
    print(f"Total score: {total}")
    print(f"Average score: {average:.1f}")
    print(f"High score: {highest}")
    print(f"Low score: {lowest}")
    print(f"Score range: {range_val}")
    
if __name__ == "__main__":
    main()