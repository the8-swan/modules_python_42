from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform

print("=== DataDeck Tournament Platform ===\n")

tournamentPlatform = TournamentPlatform()
fire_dragon = TournamentCard("dragon_001", "Fire Dragon", 5,
                             "Common", 1200, 10, 6)
ice_wizard = TournamentCard("wizard_001", "Ice Wizard", 4,
                            "Legendary", 1150, 2, 6)

print("Registering Tournament Cards...\n")

cards = [fire_dragon, ice_wizard]
for card in cards:
    print(tournamentPlatform.register_card(card))
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {card.get_rank_info()}")
    record = card.get_tournament_stats()
    print(f"- Record: {record['wins']} - {record['loses']}\n")


print("Creating tournament match...")

print(f"Match result: {tournamentPlatform.create_match('dragon_001',
                                                       'wizard_001')}\n")

print("Tournament Leaderboard:")
leaderboard = tournamentPlatform.get_leaderboard()
for classement in leaderboard:
    print(f"- {classement}")


print("\nPlatform Report:")
print(f"{tournamentPlatform.generate_tournament_report()}\n")

print("=== Tournament Platform Successfully Deployed! ===")
print("All abstract patterns working together harmoniously!")
