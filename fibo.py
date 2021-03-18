# fibo.py

def main():
    print("This program determines the nth Fibonacci number.")
    n = int(input("Enter a positive, non-0 number: "))
    print("The", str(n) + "th number of the Fibonacci sequence is", fib(n))


def fib(n):
    if n == 0 or n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


main()
