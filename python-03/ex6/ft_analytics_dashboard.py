

def list_comprehensions_demo(scores: dict[str, int]) -> None:
    """Demonstrates list comprehensions for filtering and transforming[cite: 388, 397]."""
    print("=== List Comprehension Examples ===")
    
    high_scorers = [player for player, score in scores.items() if score > 2000]
    print(f"High scorers (>2000): {high_scorers}")
    
    scores_doubled = [score * 2 for score in scores.values()]
    print(f"Scores doubled: {scores_doubled}")
    
    active_players = [player for player in scores.keys()]
    print(f"Active players: {active_players}\n")


def dict_comprehensions_demo(scores: dict[str, int], achievements: dict[str, set[str]]) -> None:
    """Demonstrates dict comprehensions for mappings and counting[cite: 389, 398]."""
    print("=== Dict Comprehension Examples ===")
    
    player_scores = {player: score for player, score in scores.items()}
    print(f"Player scores: {player_scores}")
    
    score_categories = {
        'high': len([s for s in scores.values() if s > 2000]),
        'medium': len([s for s in scores.values() if 1900 <= s <= 2000]),
        'low': len([s for s in scores.values() if s < 1900])
    }
    print(f"Score categories: {score_categories}")
    
    achievement_counts = {player: len(achvs) for player, achvs in achievements.items()}
    print(f"Achievement counts: {achievement_counts}\n")


def set_comprehensions_demo(scores: dict[str, int], achievements: dict[str, set[str]]) -> None:
    """Demonstrates set comprehensions for finding unique values[cite: 390, 399]."""
    print("=== Set Comprehension Examples ===")
    
    unique_players = {player for player in scores.keys()}
    print(f"Unique players: {unique_players}")
    
    unique_achievements = {achv for achvs in achievements.values() for achv in achvs}
    print(f"Unique achievements: {unique_achievements}")
    
    regions = ["north", "east", "central", "north", "east"]
    active_regions = {region for region in regions}
    print(f"Active regions: {active_regions}\n")


def main() -> None:
    """
    Main function representing the Game Analytics Dashboard.
    Combines all data structures and comprehensions[cite: 385, 400].
    """
    print("=== Game Analytics Dashboard ===\n")
    
    player_scores: dict[str, int] = {
        'alice': 2300, 
        'bob': 1800, 
        'charlie': 2150, 
        'diana': 1900
    }
    
    player_achievements: dict[str, set[str]] = {
        'alice': {'first_kill', 'level_10', 'boss_slayer', 'speed_demon', 'collector'},
        'bob': {'first_kill', 'level_10', 'boss_slayer'},
        'charlie': {'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon', 'perfectionist', 'explorer'},
        'diana': {'first_kill', 'level_10'}
    }

    list_comprehensions_demo(player_scores)
    dict_comprehensions_demo(player_scores, player_achievements)
    set_comprehensions_demo(player_scores, player_achievements)
    
    print("=== Combined Analysis ===")
    total_players = len(player_scores)
    
    total_unique_achvs = len({a for achvs in player_achievements.values() for a in achvs})
    
    average_score = sum(player_scores.values()) / total_players
    
    top_player = ""
    top_score = -1
    for p, s in player_scores.items():
        if s > top_score:
            top_score = s
            top_player = p
            
    top_achvs = len(player_achievements[top_player])

    print(f"Total players: {total_players}")
    print(f"Total unique achievements: {total_unique_achvs}")
    print(f"Average score: {average_score:.1f}")
    print(f"Top performer: {top_player} ({top_score} points, {top_achvs} achievements)")


if __name__ == "__main__":
    main()