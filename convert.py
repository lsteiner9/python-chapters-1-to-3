# convert.py

def main():
    print("This program converts temperature from degrees Celsius to degrees Fahrenheit.")
    for i in range(101):
        fahrenheit = (9.0 / 5.0) * i + 32
        print(i, "degrees Celsius is", fahrenheit, "degrees Fahrenheit.")

    print("This program converts temperature from degrees Fahrenheit to degrees Celsius.")
    for i in range(101):
        celsius = (9.0 / 5.0) * i + 32
        print(i, "degrees Fahrenheit is", celsius, "degrees Celsius.")


main()
