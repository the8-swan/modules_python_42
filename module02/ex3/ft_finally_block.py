#!/usr/bin/env python3
def water_plants(plant_list):
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise Exception()
            print("Watering", plant)
    except Exception:
        print("Error: Cannot water None - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    plants = ['Tulip', 'Rose', 'Lilies', 'Sunflowers']
    water_plants(plants)
    print("Watering completed successfully!")
    print("")
    print("Testing with error...")
    plants_error = ['Tulip', None, 'Lilies', 'Sunflowers']
    water_plants(plants_error)
    print("")
    print("Cleanup always happens, even with errors!")


print("=== Garden Watering System ==")
test_watering_system()
