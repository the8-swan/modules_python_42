#!/usr/bin/env python3

def check_plant_health(
                    plant_name: str,
                    water_level: int,
                    sunlight_hours: int):
    if plant_name == "" or plant_name is None:
        raise ValueError("Error: Plant name cannot be empty!")
    if water_level > 10:
        raise ValueError(
            "Error:"
            f"Water level {water_level} is too high (max 10)")
    if water_level < 1:
        raise ValueError(
            "Error:"
            "Water level {water_level} is too low (min 1)")
    if sunlight_hours > 12:
        raise ValueError(
            "Error:"
            f"Sunlight hours {sunlight_hours} is too hight (max 12)")
    if sunlight_hours < 2:
        raise ValueError(
            "Error:"
            "Sunlight hours {sunlight_hours} is too low (min 2)")
    return f"Plant {plant_name} is healthy!"


def test_plant_checks():
    tests = [
        ("tomato", 9, 5),
        (None, 9, 5),
        ("tomato", 17, 5),
        ("tomato", 7, -2)
    ]
    for test in tests:
        try:
            result = check_plant_health(
                test[0],
                test[1],
                test[2]
            )
            print(result)
        except ValueError as e:
            print(e)


print("=== Garden Plant Health Checker ===")
test_plant_checks()
print("All error raising tests completed!")
