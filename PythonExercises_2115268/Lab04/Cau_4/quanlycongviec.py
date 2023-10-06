from tkinter import *
from tkinter import messagebox

tasks_list = []
counter = 1
 
def inputError() :
    if enterTaskField.get() == "" :
         
        # show the error message
        messagebox.showerror("Input Error")
        return 0
    return 1

def clear_taskNumberField() :
    taskNumberField.delete(0.0, END)
  
def clear_taskField() :
    enterTaskField.delete(0, END)
    
def insertTask():
    
    global counter
     
    # kiem tra loi
    value = inputError()
    if value == 0 :
        return
 
    content = enterTaskField.get() + "\n"
    tasks_list.append(content)
    
    TextArea.insert('end -1 chars', "[ " + str(counter) + " ] " + content)
    counter += 1
    clear_taskField()
def delete() :
     
    global counter
    if len(tasks_list) == 0 :
        messagebox.showerror("No task")
        return
    number = taskNumberField.get(1.0, END)
 
    if number == "\n" :
        messagebox.showerror("input error")
        return
     
    else :
        task_no = int(number)
 
    clear_taskNumberField()
    tasks_list.pop(task_no - 1)
 
    counter -= 1
    TextArea.delete(1.0, END)

    for i in range(len(tasks_list)) :
        TextArea.insert('end -1 chars', "[ " + str(i + 1) + " ] " + tasks_list[i])
     
if __name__ == "__main__" :
    gui = Tk()
    gui.configure(background = "light blue")
    gui.title("Quản lý công việc")
    gui.geometry("250x300")
    enterTask = Label(gui, text = "Nhập nhiệm vụ của bạn",bg = "light blue")
    enterTaskField = Entry(gui)
    Submit = Button(gui, text = "Nộp", fg = "Black", bg = "white", command = insertTask)
    TextArea = Text(gui, height = 5, width = 25, font = "lucida 13")
    taskNumber = Label(gui, text = "Nhập số nhiệm vụ cần xóa", bg = "light blue")                      
    taskNumberField = Text(gui, height = 1, width = 2, font = "lucida 13")
    delete = Button(gui, text = "Xóa", fg = "Black", bg = "white", command = delete)
    Exit = Button(gui, text = "Thoát", fg = "Black", bg = "gray", command = exit)
    enterTask.grid(row = 0, column = 2)              
    enterTaskField.grid(row = 1, column = 2, ipadx = 50)
    Submit.grid(row = 2, column = 2)
    
    TextArea.grid(row = 3, column = 2, padx = 10, sticky = W)
                        
    taskNumber.grid(row = 4, column = 2, pady = 5)
                        
    taskNumberField.grid(row = 5, column = 2)
                     
    delete.grid(row = 6, column = 2, pady = 5)
                        
    Exit.grid(row = 7, column = 2)
    
    gui.mainloop()