from ex3.CardFactory import CardFactory
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard 
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
import random


class FantasyCardFactory(CardFactory):
	def __init__(self):
		self.cards = []
		self.cardsnumber = 0
		self.creatures = [{'Fire Dragon':5}, {'Goblin Warrior':2}]
		self.spells = [{'Lightning Bolt':3}]
		self.artifacts=[{'Mana Crystal': 2}]

	def create_creature(self, name_or_power) -> Card:
		for creature in self.creatures:
			for name, cost in creature.items():
				if name == name_or_power or cost == name_or_power:
					obj = CreatureCard(name, cost, "Legendary", 7, 5)
					return obj

	def create_spell(self, name_or_power) -> Card:
		for spell in self.spells:
			for name, cost in spell.items():
				if name == name_or_power or cost == name_or_power:
					obj = SpellCard(name, cost, "Common",'damage')
					return obj

	def create_artifact(self, name_or_power) -> Card:
		for artifact in self.artifacts:
			for name, cost in artifact.items():
				if name == name_or_power or cost == name_or_power:
					obj = ArtifactCard(name, cost, 'Common', 5, 'Permanent: +1 mana per turn')
					return obj

	def create_themed_deck(self, size: int) -> dict:
		types = [self.creatures, self.spells, self.artifacts]
		print("[",end='')
		for i in range(size):
			typ = random.choice(types)
			card = typ[random.randint(0, len(typ)-1)]
			for key in card:
				if typ == types[0]:
					obj = self.create_creature(key)
				elif typ == types[1]:
					obj = self.create_spell(key)
				else:
					obj = self.create_artifact(key)
				print(f"{obj.name} ({obj.cost})",end='')
				self.cards.append(obj)
			if i != size-1:
				print(", ",end=' ')
		print("]")
		return {
			"cards": self.cards
		}


	def get_supported_types(self) -> dict:
	    return {
			'creatures': ['dragon', 'goblin'],
			'spells': ['fireball'],
			'artifacts': ['mana_ring']
		}