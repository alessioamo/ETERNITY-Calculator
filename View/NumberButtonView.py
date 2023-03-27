import customtkinter as ctk
from Widget.Button.GeneralCalculatorButton import CalculatorButton


class NumberButtonView(ctk.CTkFrame):
    def __init__(self, parentContainer):
        super().__init__(parentContainer, fg_color="yellow", width=400, height=140)
        self.pack_propagate(False)

        btn1 = CalculatorButton(parentContainer=self, symbol='1')
        btn1.pack()
