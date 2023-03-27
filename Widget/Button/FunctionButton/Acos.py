from Widget.Button.GeneralCalculatorButton import CalculatorFunctionButton


class AcosButton(CalculatorFunctionButton):
    def __init__(self, parentContainer, symbol):
        super().__init__(parentContainer, symbol)

    def compute(self, *arg):
        (input) = arg
        return input*3
