#!/usr/bin/env python3

class GardenError(Exception):
    """ A basic error for garden problems"""
    pass


class PlantError(GardenError):
    """For problems with plants (inherits from GardenError)"""
    pass


class WaterError(GardenError):
    """For problems with plants (inherits from GardenError)"""
    pass


def test_custom_exceptions():
    """ Function that raise different custom errors and catches them."""
    print("=== Custom Garden Errors Demo ===")
    print("")
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
        if water < 0:
            raise WaterError(
                    "Caught WaterError:"
                    "Not enough water in the tank!")
    except WaterError as e:
        print(e)

    print("")
    print("Testing catching all garden errors...")
    errors = [
        WaterError("Caught WaterError: Not enough water in the tank!"),
        PlantError("Caught PlantError: The rose plant is wilting!")
        ]
    for error in errors:
        try:
            raise error
        except GardenError as e:
            print(f"{e}")
    print("All custom error types work correctly!")


test_custom_exceptions()
