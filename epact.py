# epact.py

def main():
    print("This program determines the number of days for the Gregorian epact.")
    year = int(input("Enter a four-digit year: "))
    c = year / 100
    epact = (8 + (c / 4) - c + ((8 * c + 13) / 25) + 11 * (year % 19)) % 30
    print("The value of the epact is", epact)


main()
