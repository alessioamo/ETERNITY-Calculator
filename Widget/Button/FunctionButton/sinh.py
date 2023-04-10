from View.OutputView import ResultEntry
from Widget.Button.GeneralCalculatorButton import CalculatorFunctionButton
from Error.InvalidInputError import InvalidInputError
from Error.ErrorMessages import ErrorMessages

# def sinh(x):
#    e = 2.71828
#    return (e ** x - e ** (-x)) / 2


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def power(args):
    base = args[0]
    exp = args[1]
    return base ** exp


def to_radians(degrees):
    pi = 3.14159265359
    radians = degrees * (pi / 180)
    return radians


class SinhButton(CalculatorFunctionButton):
    def __init__(self, parentContainer, symbol):
        super().__init__(parentContainer, symbol)

    def compute(self, args):
        if len(args) == 1 or (len(args) == 2 and args[1] == 0):
            num = args[0]
        elif len(args) == 2 and args[1] == 1:
            num = to_radians(args[0])
        else:
            raise Exception("Invalid input: sinh takes 1 input which is the "
                            "number in degrees, or 2 inputs which is the number "
                            "and whether the number is in \" radians\" or \" "
                            "degrees\".")
        result = 0
        pi = 3.14159265359
        twopi = 2 * pi

        # if num is too big, convert to interval 0 -> 2pi
        num = num % twopi

        # using for loop to create summation i=0 to i=79
        for i in range(80):
            result += (power([-1, i])) \
                * (power([num, (2 * i + 1)])) \
                / (factorial(2 * i + 1))
        return result
