from Widget.Button.GeneralCalculatorButton import CalculatorFunctionButton
from Error.InvalidInputError import InvalidInputError
from Error.ErrorMessages import ErrorMessages


class AcosButton(CalculatorFunctionButton):
    def __init__(self, parentContainer, symbol):
        super().__init__(parentContainer, symbol)

    def compute(self, *args):
        x = args[0]
        if (x == 1):
            raise InvalidInputError(
                ErrorMessages["Functions"]["Acos"]["InvalidInputOf1"])

        return 45 * x