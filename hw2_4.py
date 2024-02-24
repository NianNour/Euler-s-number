""" This is the answer for questin 4."""

def power(num1, num2: int) -> int:
    """ This is a function for power. """
    return num1 ** num2


def factorial(number: int) -> int:
    """ This is a function for factorial"""
    if number == 0:
        return 1
    return number * factorial(number - 1)


def e_func(x: int) -> float:
    """ This is a function to calculate e^x. """
    res = 1
    for number in range(1, 100):
        res = res + (power(x, number)/factorial(number))
    return res


def main():
    """ main function. """
    x = int(input("Enter x: "))
    print(e_func(x))


if __name__ == "__main__":
    main()
