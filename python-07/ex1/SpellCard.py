from ex0.Card import Card


class SpellCard(Card):
    def __init__(
        self, name: str, cost: int, rarity: str, effect_type: str
    ):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        effect_msg = (
            "Deal 3 damage to target"
            if self.name == "Lightning Bolt"
            else f"Cast {self.effect_type} spell"
        )
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": effect_msg
        }

    def resolve_effect(self, targets: list) -> dict:
        return {
            "spell": self.name,
            "targets": targets,
            "resolved": True
        }
