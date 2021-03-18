# change.py

def main():
    print("Change Counter")
    print()
    print("Please enter the count of each coin type.")
    quarters = float(input("Quarters: "))
    dimes = float(input("Dimes: "))
    nickels = float(input("Nickles: "))
    pennies = float(input("Pennies: "))
    total = quarters * .25 + dimes * .10 + nickels * .05 + pennies * .01
    print()
    print("The total value of your change is", total)


main()
