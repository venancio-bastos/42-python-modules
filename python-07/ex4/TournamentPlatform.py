from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self):
        self.cards = {}
        self.matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        self.cards[card.card_id] = card
        return card.card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        c1 = self.cards.get(card1_id)
        c2 = self.cards.get(card2_id)

        if not c1 or not c2:
            raise ValueError("Cards must be registered")

        self.matches_played += 1

        if c1.calculate_rating() >= c2.calculate_rating():
            winner, loser = c1, c2
        else:
            winner, loser = c2, c1

        winner.update_wins(1)
        loser.update_losses(1)

        return {
            "winner": winner.card_id,
            "loser": loser.card_id,
            "winner_rating": winner.calculate_rating(),
            "loser_rating": loser.calculate_rating()
        }

    def get_leaderboard(self) -> list:
        sorted_cards = sorted(
            self.cards.values(),
            key=lambda c: c.calculate_rating(),
            reverse=True
        )
        return [
            {
                "name": c.name,
                "rating": c.calculate_rating(),
                "record": f"{c.wins}-{c.losses}"
            }
            for c in sorted_cards
        ]

    def generate_tournament_report(self) -> dict:
        total_cards = len(self.cards)
        total_rating = sum(
            c.calculate_rating() for c in self.cards.values()
        )
        avg = total_rating / total_cards if total_cards > 0 else 0

        return {
            "total_cards": total_cards,
            "matches_played": self.matches_played,
            "avg_rating": int(avg),
            "platform_status": "active"
        }
