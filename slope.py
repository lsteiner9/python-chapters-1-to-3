# slope.py

def main():
    print("This program calculates the slope of a line through two (non-vertical) points.")
    x1 = float(input("Enter the x of the first point."))
    y1 = float(input("Enter the y of the first point."))
    x2 = float(input("Enter the x of the second point."))
    y2 = float(input("Enter the y of the second point."))

    print("The slope is:", (y2 - y1) / (x2 - x1))


main()
