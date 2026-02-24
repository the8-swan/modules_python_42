from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.GameEngine import GameEngine

print("=== DataDeck Game Engine ===\n")
fantasyCardFactory = FantasyCardFactory()
aggressiveStrategy = AggressiveStrategy()

gameEngine = GameEngine()
gameEngine.configure_engine(fantasyCardFactory, aggressiveStrategy)

print("Configuring Fantasy Card Game...")
print(f"Factory:  {fantasyCardFactory.__class__.__name__}")
print(f"Strategy: {aggressiveStrategy.__class__.__name__} ")
print(f"Available types: {gameEngine.factory.get_supported_types()}\n")

print("Simulating aggressive turn...")
print("Hand: ", end="")
print("Actions: ", gameEngine.simulate_turn())

print("")
print(f"Game Report: {gameEngine.get_engine_status()}\n")


print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")
