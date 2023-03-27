import customtkinter as ctk


class ModeButtonView(ctk.CTkFrame):
    def __init__(self, parentContainer):
        super().__init__(parentContainer, fg_color="blue", width=400, height=32)
        self.pack_propagate(False)
