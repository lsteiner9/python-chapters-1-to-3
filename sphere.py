# sphere.py
import math


def main():
    print("This program calculates the volume and surface area of a sphere.")
    radius = float(input("Enter the radius: "))
    volume = (4 / 3) * math.pi * (radius ** 3)
    area = 4 * math.pi * (radius ** 2)
    print("The volume is", volume, "and the area is", area)


main()
