from ex2.Combatable import Combatable
from ex4.Rankable import Rankable
from ex0.Card import Card
 

class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, card_id: str, name: str, cost: int, rarity: str, rating: int, attack: int, health: int):
        super().__init__(name, cost, rarity)
        self.card_id = card_id
        self.rating = rating
        self.wins = 0
        self.loses = 0
        self.attack_power = attack
        self.health = health


    def play(self, game_state: dict) -> dict:
        pass

    def attack(self, target: "TournamentCard") -> dict:
        target.health -= self.attack_power
        return {
            'attacker_health': self.health,
            'defender_health' : target.health
    }

    def calculate_rating(self) -> int:
        return self.rating

    def get_tournament_stats(self) -> dict:
        return {
            "wins": self.wins,
            "loses": self.loses
        }

    def defend(self, incoming_damage: int) -> dict:
        target.health -= incoming_damage
        return {
            'defender': self.health,
        }

    def get_combat_stats(self) -> dict:
        pass

    def update_wins(self, wins: int) -> None:
        self.wins += wins
        self.rating += 16

    def update_losses(self, losses: int) -> None:
        self.loses += losses
        self.rating -= 16

    def get_rank_info(self) -> dict:
        return self.rating
