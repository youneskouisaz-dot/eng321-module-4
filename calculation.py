
import math


def calculate_volume(diameter, height):
    """
    Calculate the volume of a cylindrical tank.

    diameter: Tank diameter in feet.
    height: Tank height in feet.

    Returns the volume in cubic feet.
    """

    radius = diameter / 2
    volume = math.pi * radius**2 * height

    return volume


# Test using the original Excel workbook values
if __name__ == "__main__":

    diameter = 3.0
    height = 5.0

    result = calculate_volume(diameter, height)

    print("CYLINDRICAL TANK CALCULATION")
    print("----------------------------")
    print(f"Diameter: {diameter} ft")
    print(f"Height: {height} ft")
    print(f"Calculated Volume: {result:.3f} ft³")
