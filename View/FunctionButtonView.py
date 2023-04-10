import customtkinter as ctk
from Widget.Button.FunctionButton.Acos import AcosButton
from Widget.Button.FunctionButton.sinh import SinhButton
from Widget.Button.FunctionButton.MAD import MADButton
from Widget.Button.GeneralCalculatorButton import CalculatorButton
from Widget.Button.MiscellaneousButton.ComputeButton import ComputeButton
from Widget.Button.MiscellaneousButton.ClearButton import ClearButton


class FunctionButtonView(ctk.CTkFrame):
    def __init__(self, parentContainer):
        super().__init__(parentContainer, width=400, height=175)
        self.paddingBetweenGridCells = 0
        self.grid_propagate(False)

        self.grid_columnconfigure(
            (1, 2, 3, 4, 5), weight=1, pad=self.paddingBetweenGridCells)
        self.rowconfigure((1, 2, 3, 4, 5), weight=1,
                          pad=self.paddingBetweenGridCells)

        # Row 1
        leftArr = CalculatorButton(
            parentContainer=self, symbol='<-')  # To implement
        rightArr = CalculatorButton(
            parentContainer=self, symbol='->')  # To implement
        btnDel = CalculatorButton(
            parentContainer=self, symbol='DEL')  # To implement
        btnClear = ClearButton(parentContainer=self,
                               symbol='CLR')  # To implement

        leftArr.grid(column=1, row=1)
        rightArr.grid(column=2, row=1)
        btnDel.grid(column=3, row=1)
        btnClear.grid(column=4, row=1, columnspan=2)

        # Row 2
        acosBtn = AcosButton(parentContainer=self, symbol="acos")
        acosBtn.grid(column=1, row=2)

        sinhBtn = SinhButton(parentContainer=self, symbol="sinh")
        sinhBtn.grid(column=1, row=3)

        madBtn = MADButton(parentContainer=self, symbol="mad")
        madBtn.grid(column=5, row=2)
