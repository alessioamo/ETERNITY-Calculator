import customtkinter as ctk
import tkinter as tk
from EventManager import EventManager, PossibleEvents


class EquationEntry(ctk.CTkEntry):
    def __init__(self, parentContainer, width, height):
        self.value = tk.StringVar()
        super().__init__(master=parentContainer, width=width,
                         height=height, textvariable=self.value)

        EventManager.Register(
            PossibleEvents.CALCULATOR_BUTTON_PRESSED, self.printButtonSymbol)

    def printButtonSymbol(self, symbol):
        oldValue = self.value.get()
        self.value.set(f'{oldValue}{symbol}')


class ResultEntry(ctk.CTkEntry):
    functionDictionary = {}

    def __init__(self, parentContainer, width, height):
        self.value = tk.StringVar()
        super().__init__(master=parentContainer, width=width,
                         height=height, textvariable=self.value)

        EventManager.Register(
            PossibleEvents.FUNCTION_BUTTON_CREATED, self.addFunctionDefinition)

    def addFunctionDefinition(self, param):
        (symbol, computeFunction) = param
        self.functionDictionary[symbol] = computeFunction


class OutputView(ctk.CTkFrame):
    width = 400
    height = 50

    def __init__(self, parentContainer):
        super().__init__(master=parentContainer,
                         width=self.width, height=self.height, fg_color="red")
        self.pack_propagate(False)

        self.equationEntry = EquationEntry(
            parentContainer=self, width=OutputView.width, height=OutputView.height/2)
        self.equationEntry.pack()

        self.resultEntry = ResultEntry(
            parentContainer=self, width=OutputView.width, height=OutputView.height/2)
        self.resultEntry.pack()
