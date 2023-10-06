from tkinter import *
from time import sleep
from PIL import ImageTk, Image
from random import randint
from tkinter import messagebox

#from playsound import playsound

img=[0,0,0]
y=-20
x=randint(10,690)
game=Tk()
game.title("Catch Apple")
can = Canvas(master=game, width=700, height=525, background="white")
can.pack()
img[0]=ImageTk.PhotoImage(Image.open("backgr.png"))
img[1]=ImageTk.PhotoImage(Image.open("bowl.png"))
img[2]=ImageTk.PhotoImage(Image.open("apple.png"))
#background
backgr=can.create_image(0,0,anchor=NW,image=img[0])
bowl=can.create_image(0,420,anchor=NW,image=img[1])
apple=can.create_image(x,y,anchor=NW,image=img[2])
can.update()
score=0
text_score=can.create_text(620,30,text="SCORE:"+str(score), fil="red",font=("Times",20))
#ham qua tao roi
def AppleFall():
    global apple, score

    # Di chuyen qua tao xuong
    can.move(apple, 0, 10)

    # Ktra xam qua tao co roi ra khoi khung
    if can.coords(apple)[1] > 550:
        can.delete(apple)  # Delete the apple
        y = -20
        x = randint(10, 690)
        apple = can.create_image(x, y, anchor=NW, image=img[2])  # Draw a new apple
   

    #Kta xem qua tao co cham vao chen khong
    if (can.coords(apple)[0] >= can.coords(bowl)[0] and
            can.coords(apple)[0] + 50 <= can.coords(bowl)[0] + 120 and
            can.coords(apple)[1] + 50 >= can.coords(bowl)[1] and
            can.coords(apple)[1] + 50 <= can.coords(bowl)[1] + 37.5):
        can.delete(apple)  # Xoa qua tao
        y = -20
        x = randint(10, 690)
        apple = can.create_image(x, y, anchor=NW, image=img[2])  
        score += 1  
        can.itemconfig(text_score, text="SCORE:" + str(score))  #Cap nhat diem
    
    can.update()

def right():
    global bowl
    if can.coords(bowl)[0]<650:
        can.move(bowl,20,0)
    can.update()
def left():
    global bowl
    if can.coords(bowl)[0]>-10:
        can.move(bowl,-20,0)
    can.update()
def keyPress(event): #tao su kien khi nhan nut
    if event.keysym=="Right":
        right()
    if event.keysym=="Left":
        left()


def game_over_message():
    global game_over
    game_over = True
    messagebox.showinfo("Game Over", "Your score: " + str(score))
  

    
can.bind_all("<KeyPress>",keyPress)#gan su kien
gameOver=False
while not gameOver:
    AppleFall()
    sleep(0.05)
game.mainloop()
# qua tao: 50,50
# caichen: 120, 75# xtao>=xchen & xtao+120 & 
#ytao +50>=ychen & ytao+50<=ychen + 37.5