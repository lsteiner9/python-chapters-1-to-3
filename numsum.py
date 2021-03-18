# numsum.py

def main():
    print("This program determines the sum of the first n natural numbers.")
    n = int(input("Enter the number of numbers to sum: "))
    sums = 0
    for i in range (1, n):
        sums += i
    print("The sum is", sums)


main()
