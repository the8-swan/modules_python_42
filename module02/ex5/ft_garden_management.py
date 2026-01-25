
class GardenError(Exception):
    """Base exception class for garden-related errors."""
    pass


class PlantError(Exception):
    """ Exception raised when an error occurs while adding a plant."""
    def __init__(self, message):
        """ Initialize a PlantError with a descriptive message."""
        super().__init__(f"Error adding plant : {message}")


class WaterError(Exception):
    """ Exception raised when a plant's water level is invalid."""
    def __init__(self, message):
        """ Initialize a WaterError with a descriptive message."""
        super().__init__(f"Error checking {message}")


class SunError(Exception):
    """Exception raised when a plant's sunlight level is invalid."""
    def __init__(self, message):
        """Initialize a SunError with a descriptive message."""
        super().__init__(f"Error checking {message}")


class Plant:
    """Represents a plant ."""
    def __init__(self, name, water, sun):
        """Create a new Plant instance."""
        self.name = name
        self.water = water
        self.sun = sun


class GardenManager:
    """ Class that manages a collection of plants and their health."""
    def __init__(self):
        """Initialize the garden manager with an empty plant list."""
        self.plants = []

    def add_plant(self, plants):
        """Add plants to the garden after validating input."""
        print("Adding plants to garden...")
        for name, water, sun in plants:
            try:
                if name == "" or name is None:
                    raise PlantError("Plant name cannot be empty!")
                p = Plant(name, water, sun)
                self.plants.append(p)
                print(f"Added {name} successfully")
            except (PlantError, WaterError, SunError) as e:
                print(f"{e}")
        print("")

    def water_plant(self):
        """Water all plants in the garden."""
        print("Watering plants...\nOpening watering system")
        try:
            for plant in self.plants:
                print(f"Watering {plant.name} - sucess")
                plant.water += 1
        finally:
            print("Closing watering system (cleanup)")
            print("")

    def check_health(self):
        """Check the health of all plants in the garden."""
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
                    f" sun: {plant.sun})")
            except (WaterError, SunError) as a:
                print(f"{a}")
        print("")


def test_garden_management():
    """ Test the garden management system."""
    print("=== Garden Management System ===")
    print("")
    garden = GardenManager()
    plants = [
        ("tomatto", 4, 8),
        ("lettuce", 14, 6),
        ("", 5, 5)
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


test_garden_management()
