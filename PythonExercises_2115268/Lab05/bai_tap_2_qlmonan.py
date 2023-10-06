from tkinter import *
from tkinter import ttk

if __name__ == "__main__":
    root = Tk()
    root.configure(background='light gray')
    root.title("Quản lý món ăn")
    root.geometry("550x300")
    # label
    monan = Label(root, text="Nhóm món ăn", font=('Serif 8'),bg="light gray")
    
    
    #
    monan.grid(row=0, column=4)
    #
    loaimoan =ttk.Combobox(root)
    loaimoan.grid(row=0, column=6, padx=100)
    
    
    root.mainloop()