from Widget.Button.GeneralCalculatorButton import CalculatorFunctionButton
from Error.InvalidInputError import InvalidInputError
from Error.ErrorMessages import ErrorMessages
# import math


class LogButton(CalculatorFunctionButton):
    def __init__(self, parentContainer, symbol):
        super().__init__(parentContainer, symbol)

    def compute(self, *args):
        x = args[0]
        print(args)
        if (x <= 0):
            raise InvalidInputError(
                ErrorMessages["Functions"]["Log"]["InvalidInputOfNotPositive"])
        output = self.logarithm(x)
        # print("ERROR: ", abs(math.log(x) - output))
        return output
        
    def logarithm(self, x, base=10):    
        # Define epsilon for accuracy
        epsilon = 1e-10

        # Initialize variables for binary search
        lower_bound = 0
        upper_bound = x
        result = 0.0

        # Perform binary search
        while abs(x - (base ** result)) > epsilon:
            mid = (lower_bound + upper_bound) / 2
            mid_result = base ** mid
            if mid_result < x:
                lower_bound = mid
            else:
                upper_bound = mid
            result = mid

        return result