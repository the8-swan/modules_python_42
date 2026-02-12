from card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, attack: int, health: int):
        if attack < 0 or health < 0:
            raise ValueError("Attack and health should be positive integers")
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health
        self.type = "Creature"

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield",
        }

    def attack_target(self, target) -> dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage_dealt": self.attack,
            "combat_resolved": True,
        }

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info.update({"type": self.type, "attack": self.attack, "health": self.health})
        return info
