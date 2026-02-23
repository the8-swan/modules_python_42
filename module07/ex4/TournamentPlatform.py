from ex4.TournamentCard import TournamentCard
class TournamentPlatform:
    def __init__(self):
        self.cards = []

    def register_card(self, card: TournamentCard) -> str:
        self.cards.append(card)
        return f"{card.name}"

    
