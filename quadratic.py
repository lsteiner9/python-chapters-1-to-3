# quadratic.py

import math


def main():
    print("This program finds the real solutions to a quadratic\n")

    a = float(input("Please enter the coefficients (a, b, c, separated by enter): "))
    b = float(input())
    c = float(input())

    root = math.sqrt(b * b - 4 * a * c)
    root1 = (-b + root) / (2 * a)
    root2 = (-b - root) / (2 * a)

    print("\nThe solutions are:", root1, root2)


main()
