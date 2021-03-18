# average.py

def main():
    print("This program determines the average of a series of numbers.")
    number = int(input("Enter the number of inputs: "))
    sums = 0
    for i in range(number):
        sums += input("Enter a number: ")
    print("The average is", sums / float(number))


main()
