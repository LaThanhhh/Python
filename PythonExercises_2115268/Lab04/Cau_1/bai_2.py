from PLL import Image, ImageTk
from tkinter import Tk, Label, BOTH
from tkinter.ttk import Frame,  Style

class Emxaple(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Absolute positioning")
        self.pack(fill=BOTH, expand=1)

        Style().configure("TFrame", background="#333")

     
