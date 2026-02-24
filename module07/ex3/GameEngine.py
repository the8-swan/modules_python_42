from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    def __init__(self) -> None:
        self.factory = None
        self.strategy = None
        self.created_cards = []
        self.mana = 6
        self.damage = 0
        self.turns = 0
        self.default_cards_created = 3

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> dict:
        mana_used = 0
        data = self.factory.create_themed_deck(self.default_cards_created)
        turn_data = self.strategy.execute_turn(data["cards"], ["Enemy Player"])
        self.created_cards = turn_data["cards"]
        for card in self.created_cards:
            mana_used += card.cost
            if hasattr(card, "attack"):
                self.damage += card.attack
            else:
                self.damage += 3
        print("\nTurn execution:")
        print(f"Strategy: {self.strategy.__class__.__name__} ")
        self.turns += 1
        return {
            "cards_played": [card.name for card in self.created_cards],
            "mana_used": mana_used,
            "targets_attacked": turn_data["targets_attacked"],
            "damage_dealt": self.damage,
        }

    def get_engine_status(self) -> dict:
        return {
            "turns_simulated": self.turns,
            "strategy_used": self.strategy.get_strategy_name(),
            "total_damage": self.damage,
            "cards_created": self.default_cards_created,
        }
