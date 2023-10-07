from tkinter import *
from time import sleep
import tkinter as tk
from PIL import ImageTk, Image
from random import randint
from tkinter import messagebox

#from playsound import playsound

img=[0,0,0]
y=-20
x=randint(10,690)
game=tk.Tk()
game.title("Catch Apple")
can = Canvas(master=game, width=700, height=525, background="white")
can.pack()
missed_apples = 0  # Tthem bien tao
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

#....
def start_game():
    global gameOver, missed_apples, score
    gameOver = False
    missed_apples = 0
    score = 0
    can.itemconfig(text_score, text="SCORE:" + str(score))
    game_loop()

# Ham vong lap 
def game_loop():
    global gameOver
    while not gameOver:
        app_fall()
        sleep(0.05)
    game_over()
#ham qua tao roi
def app_fall():
    global apple, score, missed_apples

    # Di chuyen qua tao xuong
    can.move(apple, 0, 10)

    # Ktra xam qua tao co roi ra khoi khung
    if can.coords(apple)[1] > 550:
        can.delete(apple)  # Delete the apple
        y = -20
        x = randint(10, 690)
        apple = can.create_image(x, y, anchor=NW, image=img[2])  # Draw a new apple
        missed_apples += 1  # Tăng số trái táo đã bỏ qua
        if missed_apples >= 3:  # Kiểm tra nếu số trái táo bỏ qua đạt đến 3
            game_over()
   

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


def game_over():
    global gameOver
    gameOver = True
    messagebox.showinfo("Game Over!", "Score: " + str(score))
    game.destroy()

can.bind_all("<KeyPress>",keyPress)#gan su kien

# Thêm nút "Start Game"
start_button = Button(game, text="Start Game", command=start_game)
start_button.pack()

game.mainloop()
# qua tao: 50,50
# caichen: 120, 75# xtao>=xchen & xtao+120 & 
#ytao +50>=ychen & ytao+50<=ychen + 37.5
