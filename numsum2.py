# numsum2.py

def main():
    print("This program sums a series of numbers entered by the user.")
    series = int(input("Enter the number of numbers to sum: "))
    sums = 0
    for i in range(series):
        sums += int(input("Enter a number to sum: "))
    print("The sum is", sums)


main()
