from ex0.Card import Card
from tools.card_generator import CardGenerator

data = [
    {"name": "Lightning Bolt","cost": 3, "rarity": "Common", "effect_type": "damage"},
    {"name": "Healing Potion", "cost": 2, "rarity": "Common", "effect_type": "heal"},
    {"name": "Fireball", "cost": 4, "rarity": "Uncommon", "effect_type": "damage"},
    {"name": "Shield Spell", "cost": 1, "rarity": "Common", "effect_type": "buff"},
    {"name": "Meteor", "cost": 8, "rarity": "Legendary", "effect_type": "damage"},
    {"name": "Ice Shard", "cost": 2, "rarity": "Common", "effect_type": "damage"},
    {"name": "Divine Light", "cost": 5, "rarity": "Rare", "effect_type": "heal"},
    {"name": "Magic Missile", "cost": 1, "rarity": "Common", "effect_type": "damage"},
]

class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        ...

    def resolve_effect(self, targets: list) -> dict:
        ...


su = CardGenerator()
li = su.get_all_spells()
print(li)
