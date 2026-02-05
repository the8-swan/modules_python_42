import sys
import math


def calculate_distance(coords):
    """ Calculate distances using the 3D Euclidean distance formula"""
    x1, y1, z1 = 0, 0, 0
    x2, y2, z2 = coords
    result = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    print(f"Distance between (0, 0, 0) and {coords} : {result:.2f}")


def test_coordinate():
    """ Test 3D coordinate system with tuple operations."""
    print("=== Game Coordinate System ===")
    if sys.argv.__len__() == 1:
        coords = (10, 20, 5)
        print("Position created:", coords)
        calculate_distance(coords)
        print("")
        print("Unpacking demonstration:")
        x, y, z = coords
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates : X={x}, Y={y}, Z={z}")
        print("")

    elif sys.argv.__len__() == 2:
        coords = []
        print("Parsing coordinates:", sys.argv[1])
        try:
            for val in sys.argv[1].
            (','):
                coords.append(int(val))
            print(f"Parsed position: {tuple(coords)}")
            calculate_distance(tuple(coords))
        except ValueError:
            print(
                "Error parsing coordinates: invalid literal"
                "for int() with ", val)
            print(
                f"Error details - Type: ValueError,"
                f"Args: (\"invalid literal for int() with base 10: '{val}'\")")
    else:
        print("Error: Invalid format. Expected three values: x, y, z.")


test_coordinate()
