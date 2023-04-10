import customtkinter as ctk
from Widget.Button.FunctionButton.Stdev import stdevButton      #yaser
from Widget.Button.FunctionButton.LeftButton import LeftButton      #yaser
from Widget.Button.FunctionButton.RightButton import RightButton      #yaser
from Widget.Button.FunctionButton.Acos import AcosButton
from Widget.Button.GeneralCalculatorButton import CalculatorButton
from Widget.Button.MiscellaneousButton.ComputeButton import ComputeButton


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
        leftArr = LeftButton(
            parentContainer=self, symbol='<-')  # Yaser
        rightArr = RightButton(
            parentContainer=self, symbol='->')  # Yaser
        btnDel = CalculatorButton(
            parentContainer=self, symbol='DEL')  # To implement
        btnClear = ComputeButton(parentContainer=self,
                                 symbol='CLR')  # To implement

        leftArr.grid(column=1, row=1)
        rightArr.grid(column=2, row=1)
        btnDel.grid(column=3, row=1)
        btnClear.grid(column=4, row=1, columnspan=2)

        # Row 2
        acosBtn = AcosButton(parentContainer=self, symbol="acos")
        acosBtn.grid(column=1, row=2)
        stdevBtn = stdevButton(parentContainer=self, symbol="stDev")    #yaser
        stdevBtn.grid(column=2, row=2)                                  #yaser
        btnComma = CalculatorButton(parentContainer=self, symbol=',')   #yaser
        btnComma.grid(column=3, row=2)                                  #yaser

