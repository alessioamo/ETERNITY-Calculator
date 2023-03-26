import EventManager
import customtkinter as ctk
# Custom Tkinter doc: https://github.com/TomSchimansky/CustomTkinter/wiki

# Create the 4 views
# Create the acos button
# Link the button with the views using the EventManager

ctk.set_appearance_mode("dark")
window = ctk.CTk()
windowWidth = 400
windowHeight = 400
window.geometry(f'{windowWidth}x{windowHeight}')

NumberButtonView = ctk.CTkFrame(window, fg_color="blue")
btn = ctk.CTkButton(NumberButtonView, width=75, height=30,
                    text="sin")
btn.pack()
NumberButtonView.pack(expand=True, fill="both")

window.mainloop()
