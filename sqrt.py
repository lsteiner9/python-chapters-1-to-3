# sqrt.py
import math


def improve(guess, n):
    return (guess + (n / guess)) / 2


def main():
    print("This program approximates (or finds) a square root.")
    n = float(input("Enter the value to square-root: "))
    num = int(input("Enter the number of times to improve the guess: "))
    guess = n / 2
    for i in range(num):
        guess = improve(guess, n)
    print("The approximated value is", guess, "and the difference from the true square root is", math.sqrt(n) - guess)


main()
