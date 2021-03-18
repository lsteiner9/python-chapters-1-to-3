# lightning.py

def main():
    print("This program determines the distance to a lightning strike.")
    time = float(input("Enter the number of seconds between the flash and the thunder."))
    print("The distance is", time * 1100 / 5280, "miles.")


main()
