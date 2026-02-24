from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def __init__(self):
        self.cards = []
        self.mana = 6
        self.counter = 0

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        for card in hand:
            if self.counter + card.cost <= self.mana :
                self.cards.append(card)
                self.counter += card.cost 
        return {
            "cards": self.cards,
            "targets_attacked": battlefield
        }

    def get_strategy_name(self) -> str:
        return "AggresiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        return available_targets

