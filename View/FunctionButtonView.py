import customtkinter as ctk
from Widget.Button.FunctionButton.Acos import AcosButton


class FunctionButtonView(ctk.CTkFrame):
    def __init__(self, parentContainer):
        super().__init__(parentContainer, fg_color="green", width=400, height=175)

        self.pack_propagate(False)

        acosBtn = AcosButton(parentContainer=self, symbol="acos")
        acosBtn.pack()
