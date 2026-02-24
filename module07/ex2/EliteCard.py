from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str, attack_power: int):
        super().__init__(name, cost, rarity)
        self.attack_power = attack_power
        self.health = 8
        self.mana = 4

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.effect,
        }

    def attack(self, target) -> dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.attack_power,
            "combat_type": "melee",
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": 4,
        }

    def channel_mana(self, amount: int) -> dict:
        self.mana += amount
        return {"channeled": amount, "total_mana": self.mana}

    def get_magic_stats(self) -> dict:
        return {"mana": self.mana}

    def defend(self, incoming_damage: int) -> dict:
        blocked = min(3, incoming_damage)
        self.health -= (incoming_damage - blocked)
        still_alive = self.health > 0
        return {"defender": self.name,
                "damage_taken": incoming_damage - blocked,
                "damage_blocked": blocked,
                "still_alive": still_alive}

    def get_combat_stats(self) -> dict:
        return {"mana": self.mana, "attacker": self.name}
