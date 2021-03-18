# pointdistance.py
import math


def main():
    print("This program determines the distance between two points.")
    x1 = float(input("Enter the x of the first point."))
    y1 = float(input("Enter the y of the first point."))
    x2 = float(input("Enter the x of the second point."))
    y2 = float(input("Enter the y of the second point."))

    print("The distance is:", math.sqrt(((y2 - y1) ** 2) / ((x2 - x1) ** 2)))


main()

