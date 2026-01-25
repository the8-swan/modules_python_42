#!/usr/bin/env python3
def water_plants(plant_list):
    """ Water a liste of plants """
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None or plant == "":
                raise Exception()
            print("Watering", plant)
    except Exception:
        print("Error: Cannot water None - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    """A function that tests water_plants, showing that cleanup always
    happens, even when there’s an error."""
    print("=== Garden Watering System ==")
    plants = ["tomato", "lettuce", "carrots"]
    water_plants(plants)
    print("Watering completed successfully!")
    print("")
    print("Testing with error...")
    plants_error = ["tomato", "", "carrots"]
    water_plants(plants_error)
    print("")
    print("Cleanup always happens, even with errors!")


test_watering_system()
