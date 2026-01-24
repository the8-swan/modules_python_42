
class GardenError(Exception):
    pass


class PlantError(Exception):
    def __init__(self, message):
        super().__init__(f"Error adding plant : {message}")


class WaterError(Exception):
    def __init__(self, message):
        super().__init__(f"Error checking {message}")


class SunError(Exception):
    def __init__(self, message):
        super().__init__(f"Error checking {message}")


class Plant:
    def __init__(self, name, water, sun):
        self.name = name
        self.water = water
        self.sun = sun


class GardenManager:
    def __init__(self):
        self.plants = []

    def add_plant(self, plants):
        print("Adding plants to garden...")
        for name, water, sun in plants:
            try:
                p = Plant(name, water, sun)
                self.plants.append(p)
                print(f"Added {name} successfully")
            except Exception as e:
                print(f"{e}")
        print("")

    def water_plant(self):
        print("Watering plants...\nOpening watering system")
        try:
            for plant in self.plants:
                print(f"Watering {plant.name} - sucess")
                plant.water += 1
        finally:
            print("Closing watering system (cleanup)")
            print("")

    def check_health(self):
        print("Checking plant health...")
        for plant in self.plants:
            try:
                if plant.water > 10:
                    raise WaterError(
                        f"{plant.name}:"
                        f"Water level {plant.water} is too high (max 10)")
                if plant.water < 1:
                    raise WaterError(
                        f"{plant.name}:"
                        f"Water level {plant.water} is too low (min 1)")
                if plant.sun > 12:
                    raise SunError(
                        f"{plant.name}:"
                        f"Sunlight hours {plant.sun} is too hight (max 12)")
                if plant.sun < 2:
                    raise SunError(
                        f"{plant.name}:"
                        f"Sunlight hours {plant.sun} is too low (min 2)")
                print(
                    f"{plant.name} healthy (water: {plant.water},"
                    f"sun: {plant.sun})")
            except (WaterError, SunError) as a:
                print(f"{a}")
        print("")


print("=== Garden Management System ===")
print("")
garden = GardenManager()
plants = [
    ("tomatto", 6, 49),
    ("carrot", 19, 98),
    ("", 87, 99),
    ("lettuce", 1, 5)
]
garden.add_plant(plants)
garden.water_plant()
garden.check_health()
print("Testing error recovery...")
try:
    raise GardenError("Caught GardenError: Not enough water in tank")
except GardenError as e:
    print(f"{e}")
print("System recovered and continuing...")
print("")
print("Garden management system test complete!")
