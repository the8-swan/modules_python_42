#!/usr/bin/env python3

class SecurePlant:
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
        print(f"Plant created: {name}")

    def set_height(self, height: int):
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected\n")
        else:
            self.__height = height
            print(f"Height updated: {self.__height} cm [OK]")

    def set_age(self, age: int):
        if age < 0:
            print(f"Invalid operation attempted: height {age}days [REJECTED]")
            print("Security: Negative age rejected\n")
        else:
            self.__age = age
            print(f"Age updated:{self.__age} days [OK]")

    def get_height(self):
        return self.__height

    def get_age(self):
        return self.__age

    def get_info(self):
        print(f"plant:{self.__name}({self.__height}cm,{self.__age} days)")


def main():
    print("=== Garden Security System ===")
    tulip = SecurePlant("Tulip", -8, -18)
    tulip.set_age(-8)
    tulip.set_height(-18)
    tulip.get_info()


if __name__ == "__main__":
    main()
