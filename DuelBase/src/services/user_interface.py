from tkinter import Tk, ttk


class UserInterface:
    def setup_screen(self, ui:Tk):
        frm = ttk.Frame(ui, padding=10)
        frm.grid()

        ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
        ttk.Button(frm, text="Quit", command=ui.destroy).grid(column=1, row=0)