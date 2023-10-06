from tkinter.ttk import Frame, Button
from tkinter import Tk, BOTH
import tkinter.messagebox as mbox

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
        
    def initUI(self):
        self.parent.title("Message Boxes")
        self.pack()
        
        error = Button(self, text="Error", command=self.onError)
        error.grid(padx=5, pady=5)
        Warning = Button(self, text="Warning", command=self.onWarn)
        Warning.grid(row=1, column=0)
        question = Button(self, text="Question", command=self.onQuest)
        question.grid(row=0, column=1)
        inform = Button(self, text="Information", command=self.onInfo)
        inform.grid(row=1, column=1)
        
    def onError(self):
        mbox.showerror("Error", "Could not open file")
        
    def onWarn(self):
        mbox.showwarning("Warninng", "Deprecated functon call")
        
    def onQuest(self):
        mbox.askquestion("Question", "Are you sure to quit?")
        
    def onInfo(self):
        mbox.showinfo("Information","Download completed")
        
root = Tk()
ex = Example(root)
root.geometry("300x150+300+300")
root.mainloop()
                