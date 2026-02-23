from ex2.Combatable import Combatable
from ex4.Rankable import Rankable
from ex0.Card import Card


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int, rarity: str, rating: int):
        super().__init__(name, cost, rarity)
        self.rating = rating


    def play(self, game_state: dict) -> dict:
        pass

    def attack(self, target) -> dict:
        pass

    def calculate_rating(self) -> int:
        pass

    def get_tournament_stats(self) -> dict:
        pass

    def defend(self, incoming_damage: int) -> dict:
        pass

    def get_combat_stats(self) -> dict:
        pass

    def update_wins(self, wins: int) -> None:
        pass

    def update_losses(self, losses: int) -> None:
        pass

    def get_rank_info(self) -> dict:
        pass
