#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def grow(self):
        self.height += 1

    def add_age(self):
        self.age += 1

    def get_info(self):
        print(f"{self.name} : {self.height}cm, {self.age} days old")


tulip = Plant("tulip", 22, 19)
counter = 0
print("=== Day 1 ===")
tulip.get_info()
print("=== Day 7 ===")
for counter in range(6):
    tulip.grow()
    tulip.add_age()
    counter += 1
tulip.get_info()
print(f"Growth this week: +{counter}cm")
