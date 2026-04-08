from ex3.GameStrategy import GameStrategy
from ex0.CreatureCard import CreatureCard


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        cards_played = []
        mana_used = 0

        for card in hand:
            if card.name in ["Goblin Warrior", "Lightning Bolt"]:
                cards_played.append(card.name)
                mana_used += card.cost

        return {
            "cards_played": cards_played,
            "mana_used": mana_used,
            "targets_attacked": ["Enemy Player"],
            "damage_dealt": 8
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        return [
            t for t in available_targets if "Player" in t
        ] + [
            t for t in available_targets if "Player" not in t
        ]
