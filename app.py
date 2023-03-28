import tkinter as tk
from View.OutputView import OutputView
from View.FunctionButtonView import FunctionButtonView
from View.ModeButtonView import ModeButtonView
from View.NumberButtonView import NumberButtonView
import customtkinter as ctk
# Custom Tkinter doc: https://github.com/TomSchimansky/CustomTkinter/wiki

# Create the tickets for the button
# Update the ReadME
# Update Cursor position to be between brackets when function click symbol
# Fix screen dimension
# Change name and logo of calculator window
# Add Error handling for letters input
# Add left,right,delete and clear btn
# Add the function btn
# Update the image of the window calculator


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        windowWidth = 400
        windowHeight = 430
        self.geometry(f'{windowWidth}x{windowHeight}')
        self.title("Eternity - Team A")
        self.resizable(width=False, height=False)
        self.outputView = OutputView(parentContainer=self)
        self.modeButtonView = ModeButtonView(parentContainer=self)
        self.functionButtonView = FunctionButtonView(parentContainer=self)
        self.numberButtonView = NumberButtonView(parentContainer=self)

        self.outputView.pack()
        self.modeButtonView.pack()
        self.functionButtonView.pack()
        self.numberButtonView.pack()


ctk.set_appearance_mode("dark")
window = App()
window.mainloop()
