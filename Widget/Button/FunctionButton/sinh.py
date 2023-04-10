from Widget.Button.GeneralCalculatorButton import CalculatorFunctionButton
from Error.InvalidInputError import InvalidInputError
from Error.ErrorMessages import ErrorMessages


MyEulerConstant = 2.718281828459045
pi = 3.141592653589793


class SinhButton(CalculatorFunctionButton):
    def __init__(self, parentContainer, symbol):
        super().__init__(parentContainer, symbol)

    """
    Compute the hyperbolic sine of x using the formula (e^x - e^(-x)) / 2
    Args: x is a number in radians
    Returns: The hyperbolic sine of x
    """

    def sinh(self, x):
        return (MyEulerConstant**x - MyEulerConstant**(-x)) / 2

    # Checks that an argument is provided
    def compute(self, *args):
        if len(args) != 1:
            raise InvalidInputError("Error! No Input Found")

        x = args[0]
        result = self.sinh(x)
        return result
