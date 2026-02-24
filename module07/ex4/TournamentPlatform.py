from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self):
        self.cards = []
        self.match = 0

    def register_card(self, card: TournamentCard) -> str:
        self.cards.append(card)
        return f"{card.name} (ID: {card.card_id}):"

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        card_1 = None
        card_2 = None

        for card in self.cards:
            if card.card_id == card1_id:
                card_1 = card
            elif card.card_id == card2_id:
                card_2 = card

        card_1.attack(card_2)
        card_2.attack(card_1)

        if card_1.health > card_2.health:
            winner, loser = card_1, card_2
        else:
            winner, loser = card_2, card_1

        winner.update_wins(1)
        loser.update_losses(1)
        self.match += 1
        return {
            "winner": winner.card_id,
            "loser": loser.card_id,
            "winner_rating": winner.get_rank_info(),
            "loser_rating": loser.get_rank_info(),
        }

    def get_leaderboard(self) -> list:
        sorted_cards = sorted(self.cards,
                              key=lambda card: card.rating, reverse=True)
        return [
            f"{card.name} - Rating: {card.calculate_rating()}"
            f"({card.wins} - {card.loses})"
            for card in sorted_cards
        ]

    def generate_tournament_report(self) -> dict:
        summ = 0
        total_cards = len(self.cards)
        for card in self.cards:
            summ += card.rating
        return {
            "total_cards": total_cards,
            "matches_played": self.match,
            "avg_rating": 0 if total_cards == 0 else int(summ / total_cards),
            "platform_status": "active",
        }
