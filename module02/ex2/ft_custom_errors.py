#!/usr/bin/env python3

class GardenError(Exception):
    pass

class PlantError(GardenError):
    pass

class WaterError(GardenError):
    pass

def test_custom_exceptions():
    print("Testing PlantError...")
    plant = "tomato"
    try:
        raise PlantError(f"Caught PlantError: The {plant} plant is wilting!")
    except PlantError as e:
        print(e)


    print("")
    print("Testing WaterError...")
    try:
        water = -1
        if water < 0 :
            raise WaterError("Caught WaterError: Not enough water in the tank!")
    except WaterError as e:
        print(e)
    
    print("")
    print("Testing catching all garden errors...")
    try:
        raise WaterError("Caught WaterError: Not enough water in the tank!")
        raise PlantError(f"Caught PlantError: The {plant} plant is wilting!")
    except GardenError as e :
        print(f"Caught a garden error: {e}")
    print("All custom error types work correctly!")



print("=== Custom Garden Errors Demo ===")
print("")
test_custom_exceptions()