from ex2.EliteCard import EliteCard

print("=== DataDeck Ability System ===\n")
print("EliteCard capabilities:")
data = [
    {"Card": ["play", "get_card_info", "is_playable"]},
    {"Compatable:": ["attack", "defend", "get_combat_stats"]},
    {"Magical": ["cast_spell", "channel_mana", "get_magic_stats"]},
]

for d in data:
    for name, function in d.items():
        print(f"- {name}: {function}")
print("")
print("Playing Arcane Warrior (Elite Card):\n")
print("Combat phase:")

eliteCard = EliteCard("Arcane Warrior", 5, "damage", 5)
print(f"Attack result: {eliteCard.attack('Enemy')}")
print(f"Defense result: {eliteCard.defend(5)}\n")

print("Magic phase:")
print(f"Spell cast: {eliteCard.cast_spell('Fireball', ['Enemy1', 'Enemy2'])}")
print(f"Mana channel: {eliteCard.channel_mana(3)}\n")

print("Multiple interface implementation successful!")
