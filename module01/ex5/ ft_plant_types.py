#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.__name = name
        if height < 0:
            print(f"Invalid height: {height}. Reset to 0.")
            self.__height = 0
        else:
            self.__height = height
        if age < 0:
            print(f"Invalid age: {age}. Reset to 0.")
            self.__age = 0
        else:
            self.__age = age

    def get_info(self):
        return f"{self.__height}cm,{self.__age} days"


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print(f"{self._Plant__name} is blooming beautifully!")

    def get_info(self):
        print(f"{self._Plant__name} (Flower): {super().get_info()}, {self.color} color")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, td: int):
        super().__init__(name, height, age)
        self.td = td

    def produce_shade(self):
        print(f"{self._Plant__name} provides 78 square meters of shade")
	
    def get_info(self):
        print(f"{self._Plant__name} (Tree): {super().get_info()}, {self.td}cm diameter")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int, harvest_season: str):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season

    def nutritional_value(self):
        print(f"{self._Plant__name} is rich in vitamin C")
	
    def get_info(self):
        print(f"{self._Plant__name} (Vegetable): {super().get_info()}, {self.harvest_season} harvest")


def main():
    print("=== Garden Plant Types ===")
    tulip = Flower("tulipa", 18, 8, "white")
    tulip.get_info()
    tulip.bloom()

    arbre = Tree("arbre", 18, 8, 2026)
    arbre.get_info()
    arbre.produce_shade()

    tomato = Vegetable("tomato", 18, 8, "summer")
    tomato.get_info()
    tomato.nutritional_value()


if __name__ == "__main__":
    main()
