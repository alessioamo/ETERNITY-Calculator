# Import packages
from Widget.Button.GeneralCalculatorButton import CalculatorFunctionButton
from Error.InvalidInputError import InvalidInputError
from Error.ErrorMessages import ErrorMessages

#


class abxButton(CalculatorFunctionButton):

    def __init__(self, parentContainer, symbol):
        super().__init__(parentContainer, symbol)

    def compute(self, a, b, x):

        # Verify input
        if (a == 0) or (not isinstance(a, (int, float))):
            print("wrong!")

        if (b == 1) or (not isinstance(b, (int, float))):
            print("wrong!")

        if not isinstance(x, (int, float)):
            print("wrong!")

        return (a*(b**x))
