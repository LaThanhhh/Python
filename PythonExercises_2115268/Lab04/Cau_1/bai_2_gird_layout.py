from tkinter import Tk, W, E
from tkinter.ttk import Frame, Button, Style
from tkinter.ttk import Entry
from tkinter import *


class Example(Frame):
    #khai bao
    expression = ""
    #ham cap nhat experssion 

    def press(num):
       global expression
       expression = expression + str(num)
       equation.set(expression)
    
    #ham bieu thuc cuoi cung
    def equalpress():
        try:
            global expression
            tong = str(eval(expression))
            equation.set(tong)
            expression=""
        except:
            equation.set(" error ")
            expression = ""
      
    def clear():
        global expression
        expression = ""
        equation.set("")
 
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.initUI()
    
    def initUI(self):

        self.parent.title("Calculator")

        Style().configure("TButton", padding=(0, 5, 0, 5), font='serif 10')

        self.columnconfigure(0, pad=3)
        self.columnconfigure(1, pad=3)
        self.columnconfigure(2, pad=3)
        self.columnconfigure(3, pad=3)

        self.rowconfigure(0, pad=3)
        self.rowconfigure(1, pad=3)
        self.rowconfigure(2, pad=3)
        self.rowconfigure(3, pad=3)
        self.rowconfigure(4, pad=3)

        entry = Entry(self)
        entry.grid(row=0, columnspan=4, sticky=W+E)
        cls = Button(self, text="Cls", height="1",width="7" )
        cls.grid(row=1, column=0)
        bck =Button(self, text="Back", height="1",width="7")
        bck.grid(row=1, column=1)
        lbl = Button(self, height="1",width="7")
        lbl.grid(row=1, column=2)
        clo = Button(self, text="Close", height="1",width="7")
        clo.grid(row=1, column=3)
        sev = Button(self, text="7", height="1",width="7")
        sev.grid(row=2, column=0)
        eig = Button(self, text="8", height="1",width="7")
        eig.grid(row=2, column=1)
        nin = Button(self, text="9", height="1",width="7")
        nin.grid(row=2, column=2)
        div = Button(self, text="/", height="1",width="7")
        div.grid(row=2, column=3)

        fou = Button(self, text="4", height="1",width="7")
        fou.grid(row=3, column=0)
        fiv = Button(self, text="5", height="1",width="7")
        fiv.grid(row=3, column=1)
        six = Button(self, text="6", height="1",width="7")
        six.grid(row=3, column=2)
        mul = Button(self, text="*", height="1",width="7")
        mul.grid(row=3, column=3)

        one = Button(self, text="1", height="1",width="7")
        one.grid(row=4, column=0)
        two = Button(self, text="2", height="1",width="7")
        two.grid(row=4, column=1)
        thr =Button(self, text="3", height="1",width="7")
        thr.grid(row=4, column=2)
        mns = Button(self, text="-", height="1",width="7")
        mns.grid(row=4, column=3)

        zer = Button(self, text="0", height="1",width="7")
        zer.grid(row=5, column=0)
        dot = Button(self, text=".", height="1",width="7")
        dot.grid(row=5, column=1)
        equ = Button(self, text="=", height="1",width="7")
        equ.grid(row=5, column=2)
        pls = Button(self, text="+", height="1",width="7")
        pls.grid(row=5, column=3)
        
        self.pack()
        
root = Tk()
app = Example(root)
root.mainloop()
        