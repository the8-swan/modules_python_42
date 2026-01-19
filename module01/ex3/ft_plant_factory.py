#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def get_info(self):
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


def main():
    print("=== Plant Factory Output ===")
    plants = [
        Plant("Rose", 18, 17),
        Plant("Sunflower", 17, 8),
        Plant("tulip", 22, 19),
        Plant("Cactus", 5, 90),
        Plant("Fern", 15, 190)
    ]
    i = 0
    for plant in plants:
        plant.get_info()
        i += 1
    print(f"Total plants created: {i}")


if __name__ == "__main__":
    main()
