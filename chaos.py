# chaos.py
# A simple program illustrating chaotic behavior.

def main():
    print("This program illustrates a chaotic function")
    x = float(input("Enter a number between 0 and 1: "))
    y = float(input("Enter another number between 0 and 1:"))
    n = input("How many numbers should I print? ")
    print("input    ", x, "     ", y)
    for i in range(n):
        x = 3.9 * x * (1 - x)
        y = 3.9 * x * (1 - x)
        print(x, y)


main()
