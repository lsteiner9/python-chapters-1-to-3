# ladder.py
import math


def main():
    print("This program determines the length of a ladder leaned against a house.")
    radians = float(input("Enter the angle of the ladder in degrees: ")) * math.pi / 180
    height = float(input("Enter the height needed to reach: "))
    length = height / math.sin(radians)
    print("The length of the ladder needed is", length)


main()
