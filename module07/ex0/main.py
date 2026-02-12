from creatureCard import CreatureCard

print("=== DataDeck Card Foundation ===\n")
print("Testing Abstract Base Class Design:\n")
try:
    creatureCard = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    target = "Goblin Warrior"
    sufficient_mana = 6
    insufficient_mana = 3

    print(f"CreatureCard Info: {creatureCard.get_card_info()}\n")
    print(f"Playing Fire Dragon with {sufficient_mana} mana available:")
    print(f"Playable: {creatureCard.is_playable(sufficient_mana)}")
    print(f"Play result: {creatureCard.play(creatureCard)}\n")

    print("Fire Dragon attacks Goblin Warrior:")
    print(f"Attack result: {creatureCard.attack_target('Goblin Warrior')}\n")

    print(f"Testing insufficient mana ({insufficient_mana} available):")
    print(f"Playable: {creatureCard.is_playable(insufficient_mana)}\n")

    print("Abstract pattern successfully demonstrated!")
except ValueError as e:
    print(e)
