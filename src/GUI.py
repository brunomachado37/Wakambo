import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from typing import Callable

from Wakambo import Wakambo


class StartPage(tk.Frame):

    def __init__(self, parent: tk.Frame, controller: tk.Tk) -> None:
        
        tk.Frame.__init__(self, parent, bg = "white")
        self.controller = controller

        self.algotithm = Wakambo()

        self.setInitialScreen()      


    def run(self) -> None:

        self.algotithm.run()


    def setInitialScreen(self) -> None:

        self.addLogo()
                
        s = ttk.Style()
        s.configure('Custom.TButton', font = ("Helvetica", 18), foreground = 'grey')

        self.addButton("Start", style = "Custom.TButton", command = self.run)
        self.addButton("Exit", style = "Custom.TButton", command = self.controller.exit)


    def addLogo(self) -> None:

        logo = Image.open("../res/logo.png")
        logo = logo.resize((460, 354), Image.ANTIALIAS)
        logo = ImageTk.PhotoImage(logo)
        logo_label = tk.Label(self, image = logo, bg = "white")
        logo_label.image = logo
        logo_label.pack(pady = 20)


    def addButton(self, text: str, style: str, command: Callable) -> None:

        button = ttk.Button(self, text = text, style = style, command = command)
        button.pack(pady = 10)


class MainWindow(tk.Tk):

    def __init__(self, *args, **kwargs) -> None:

        tk.Tk.__init__(self, *args, **kwargs)
        self.title('Wakambo')

        container = tk.Frame(self, bg = "white")
        container.pack(side = "top", fill = "both", expand = True)

        self.frame = StartPage(container, self)
        self.frame.grid(row = 0, column = 0, sticky = "nsew")


    def exit(self) -> None:

        self.destroy()