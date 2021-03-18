# piapprox.py
import math


def main():
    print("This program approximates pi by summing terms of a series.")
    n = int(input("How many terms to sum? "))
    sums = 0
    for i in range(n):
        denom = (i * 2) + 1
        if i % 2 == 1:
            denom = -denom
        sums += (4 / denom)
    print(i)
    print(denom)
    print("The approximation is:", sums, "and the difference to pi is", abs(math.pi - sums))


main()
