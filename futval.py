# futval.py

def main():
    print("This program calculates the future value of an investment.")
    principal = float(input("Enter the initial principal: "))
    apr = float(input("Enter the annual interest rate: "))
    years = float(input("Enter the number of years: "))

    for i in range(years):
        principal = principal * (1 + apr)

    print("The value in", years, "years is:", principal)


main()
