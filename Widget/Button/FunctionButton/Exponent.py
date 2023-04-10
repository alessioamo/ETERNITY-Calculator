from Widget.Button.GeneralCalculatorButton import CalculatorFunctionButton
from Error.InvalidInputError import InvalidInputError
from Error.ErrorMessages import ErrorMessages


class ExponentButton(CalculatorFunctionButton):

    def __init__(self, parentContainer, symbol):
        super().__init__(parentContainer, symbol)

    def compute(self, base, power):
        result = 1
        negativeExponent = False
        if power < 0:
            negativeExponent = True
            power = power*(-1)
        while power > 0:
            # If power is even
            if power % 2 == 0:
                # Divide the power by 2
                power = power // 2
                # Multiply base to itself
                base = base * base
            else:
                # Decrement the power by 1 and make it even
                power = power - 1
                # Take care of the extra value that we took out
                # We will store it directly in result
                result = result * base

                # Now power is even, so we can follow our previous procedure
                power = power // 2
                base = base * base
        if negativeExponent == True:
            return round((1/result), 9)
        return round(result, 9)
