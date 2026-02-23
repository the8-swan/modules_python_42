from ex0.Card import Card
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex0.CreatureCard import CreatureCard
from typing import List
import random


class Deck():
    def __init__(self) -> None:
        self.cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        if card is not None:
            self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        return self.cards.pop(0) if self.cards else None

    def get_deck_stats(self) -> dict:
        creatures = 0
        spells = 0
        artifacts = 0
        counter = 0
        costs = 0
        for card in self.cards:
            if isinstance(card, SpellCard):
                spells += 1
            elif isinstance(card, ArtifactCard):
                artifacts += 1
            elif isinstance(card, CreatureCard):
                creatures += 1
            counter += 1
            costs += card.cost
        return {
            'total_cards': self.cards.__len__(),
            'creatures': creatures,
            'spells': spells,
            'artifacts': artifacts,
            'avg_cost': 0 if counter == 0 else round(costs / counter, 2)
        }
