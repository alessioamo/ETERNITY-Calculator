import customtkinter as ctk
from EventManager import EventManager, PossibleEvents


class CalculatorButton(ctk.CTkButton):
    width = 75
    height = 30

    def __init__(self, parentContainer, symbol):
        super().__init__(master=parentContainer, width=CalculatorButton.width,
                         height=CalculatorButton.height, text=symbol, command=self.onClick)
        self.symbol = symbol

    def onClick(self):
        EventManager.Notify(
            PossibleEvents.CALCULATOR_BUTTON_PRESSED, self.symbol)


class CalculatorFunctionButton(CalculatorButton):
    def __init__(self, parentContainer, symbol):
        super().__init__(parentContainer, symbol)
        EventManager.Notify(
            PossibleEvents.FUNCTION_BUTTON_CREATED, (self.symbol, self.compute))

    def compute(self, *arg):
        pass
