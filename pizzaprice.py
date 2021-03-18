# pizzaprice.py
import math


def main():
    print("This program calculates the cost per square inch of a circular pizza.")
    diameter = float(input("Enter the pizza's diameter: "))
    price = float(input("Enter the pizza's price: "))
    area = math.pi * ((diameter / 2) ** 2)
    cost = price / area
    print("The cost per square inch is", cost)


main()
