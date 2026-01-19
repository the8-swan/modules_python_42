#!/usr/bin/env python3
class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


rose = Plant("Rose", 18, 17)
sunflower = Plant("Sunflower", 17, 8)
tulip = Plant("tulip", 22, 19)
print("=== Garden Plant Registry ===")
print(f"{rose.name}: {rose.height}cm, {rose.age} days old")
print(f"{sunflower.name}: {sunflower.height}cm, {sunflower.age} days old")
print(f"{tulip.name}: {tulip.height}cm, {tulip.age} days old")
