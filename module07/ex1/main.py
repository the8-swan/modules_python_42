from ex1.Deck import Deck
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex0.CreatureCard import CreatureCard


print("=== DataDeck Deck Builder ===\n")
print("Building deck with different card types...")
cards = [
        SpellCard('Lightning Bolt', 3, 'Common', 'damage'),
        ArtifactCard('Mana Crystal', 2, 'Common', 5,
                     'Permanent: +1 mana per turn'),
        CreatureCard('Fire Dragon', 5, 'Legendary', 7, 5)
        ]

titles = [
    "Spell",
    "Artifact",
    "Creature"
]

deck = Deck()
for card in cards:
    deck.add_card(card)
print(f"Deck stats: {deck.get_deck_stats()}\n")

print("Drawing and playing cards:\n")

for card, title in zip(cards, titles):
    print(f"Drew: {card.name} ({title})")
    print(f"Play result: {card.play(None)}\n")

print("Polymorphism in action: Same interface, different card behaviors!")
