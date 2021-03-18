# molecularweight.py

def main():
    print("This program calculates the molecular weight of a hydrocarbon.")
    h = int(input("Enter the number of hydrogen atoms: "))
    c = int(input("Enter the number of carbon atoms: "))
    o = int(input("Enter the number of oxygen atoms: "))
    weight = (h * 1.0079) + (c * 12.011) + (o * 15.9994)
    print("The molecular weight is", weight)


main()
